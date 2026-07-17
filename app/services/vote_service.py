from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.vote_repository import VoteRepository
from app.repositories.voter_repository import VoterRepository
from app.repositories.candidate_repository import CandidateRepository
from app.schemas.vote import VoteCreate


class VoteService:

    def __init__(self):
        self.vote_repository = VoteRepository()
        self.voter_repository = VoterRepository()
        self.candidate_repository = CandidateRepository()

    def create_vote(self, db: Session, vote: VoteCreate):

        try:

            voter = self.voter_repository.get_by_id(
                db,
                vote.voter_id
            )

            if not voter:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Voter not found."
                )

            if voter.has_voted:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="This voter has already voted."
                )

            candidate = self.candidate_repository.get_by_id(
                db,
                vote.candidate_id
            )

            if not candidate:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Candidate not found."
                )

            new_vote = self.vote_repository.create(
                db,
                vote
            )

            voter.has_voted = True

            candidate.votes += 1

            db.commit()

            db.refresh(new_vote)

            return new_vote

        except HTTPException:
            db.rollback()
            raise

        except Exception:
            db.rollback()
            raise HTTPException(
                status_code=500,
                detail="Internal server error."
            )

    def get_all_votes(self, db: Session):

        return self.vote_repository.get_all(db)