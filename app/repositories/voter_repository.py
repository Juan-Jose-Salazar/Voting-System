from sqlalchemy.orm import Session

from app.models.voter import Voter
from app.schemas.voter import VoterCreate


class VoterRepository:

    @staticmethod
    def create(db: Session, voter: VoterCreate) -> Voter:
        new_voter = Voter(
            name=voter.name,
            email=voter.email
        )

        db.add(new_voter)
        

        return new_voter

    @staticmethod
    def get_by_id(db: Session, voter_id: int) -> Voter | None:
        return db.query(Voter).filter(Voter.id == voter_id).first()

    @staticmethod
    def get_by_email(db: Session, email: str) -> Voter | None:
        return db.query(Voter).filter(Voter.email == email).first()

    @staticmethod
    def get_by_name(db: Session, name: str) -> Voter | None:
        return db.query(Voter).filter(Voter.name == name).first()

    @staticmethod
    def delete(db: Session, voter: Voter):
        db.delete(voter)

    
    def count_voters_voted(self, db: Session) -> int:
        return (
            db.query(Voter)
            .filter(Voter.has_voted == True)
            .count()
        )
    
    
    def get_all(self, db: Session):
        return db.query(Voter).all()