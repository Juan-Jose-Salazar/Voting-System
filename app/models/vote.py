from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base



class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, index=True)

    voter_id = Column(
        Integer,
        ForeignKey("voters.id"),
        unique=True,
        nullable=False
    )

    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id"),
        nullable=False
    )

    voter = relationship(
        "Voter",
        back_populates="vote"
    )

    candidate = relationship(
        "Candidate",
        back_populates="vote_records"
    )