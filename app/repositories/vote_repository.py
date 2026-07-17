from sqlalchemy.orm import Session

from app.models.vote import Vote
from app.schemas.vote import VoteCreate


class VoteRepository:

    @staticmethod
    def create(db: Session, vote: VoteCreate):

        new_vote = Vote(
            voter_id=vote.voter_id,
            candidate_id=vote.candidate_id
        )

        db.add(new_vote)

        return new_vote

    @staticmethod
    def get_all(db: Session):

        return db.query(Vote).all()