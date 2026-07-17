from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.voter_repository import VoterRepository
from app.repositories.candidate_repository import CandidateRepository
from app.schemas.voter import VoterCreate


class VoterService:

    def __init__(self):
        self.voter_repository = VoterRepository()
        self.candidate_repository = CandidateRepository()

    def create_voter(self, db: Session, voter: VoterCreate):

        try:

            if self.voter_repository.get_by_email(db, voter.email):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already registered."
                )

            if self.candidate_repository.get_by_name(db, voter.name):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="A candidate cannot be registered as a voter."
                )

            new_voter = self.voter_repository.create(db, voter)

            db.commit()
            db.refresh(new_voter)

            return new_voter

        except HTTPException:
            db.rollback()
            raise

        except Exception:
            db.rollback()
            raise HTTPException(
                status_code=500,
                detail="Internal server error."
            )

    def delete_voter(self, db: Session, voter_id: int):

        try:

            voter = self.voter_repository.get_by_id(db, voter_id)

            if not voter:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Voter not found."
                )

            self.voter_repository.delete(db, voter)

            db.commit()

            return {
                "message": "Voter deleted successfully."
            }

        except HTTPException:
            db.rollback()
            raise

        except Exception:
            db.rollback()
            raise HTTPException(
                status_code=500,
                detail="Internal server error."
            )