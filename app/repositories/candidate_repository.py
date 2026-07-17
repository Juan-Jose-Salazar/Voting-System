from sqlalchemy.orm import Session

from app.models.candidate import Candidate
from app.schemas.candidate import CandidateCreate


class CandidateRepository:

    @staticmethod
    def create(db: Session, candidate: CandidateCreate) -> Candidate:

        new_candidate = Candidate(
            name=candidate.name,
            party=candidate.party
        )

        db.add(new_candidate)
        

        return new_candidate

    @staticmethod
    def get_by_id(db: Session, candidate_id: int) -> Candidate | None:

        return (
            db.query(Candidate)
            .filter(Candidate.id == candidate_id)
            .first()
        )

    @staticmethod
    def get_by_name(db: Session, name: str) -> Candidate | None:

        return (
            db.query(Candidate)
            .filter(Candidate.name == name)
            .first()
        )

    
    def get_all(self, db: Session):

        return db.query(Candidate).all()