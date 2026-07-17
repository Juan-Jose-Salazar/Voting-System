from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.candidate_repository import CandidateRepository
from app.repositories.voter_repository import VoterRepository
from app.schemas.candidate import CandidateCreate


class CandidateService:

    def __init__(self):
        self.candidate_repository = CandidateRepository()
        self.voter_repository = VoterRepository()

    def create_candidate(self, db: Session, candidate: CandidateCreate):

        try:

            if self.candidate_repository.get_by_name(db, candidate.name):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Candidate already exists."
                )

            if self.voter_repository.get_by_name(db, candidate.name):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="A voter cannot be registered as a candidate."
                )

            new_candidate = self.candidate_repository.create(
                db,
                candidate
            )

            db.commit()
            db.refresh(new_candidate)

            return new_candidate

        except HTTPException:
            db.rollback()
            raise

        except Exception:
            db.rollback()
            raise HTTPException(
                status_code=500,
                detail="Internal server error."
            )

    def get_all_candidates(self, db: Session):

        return self.candidate_repository.get_all(db)