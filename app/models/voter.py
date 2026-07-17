from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.database import Base


class Voter(Base):
    __tablename__ = "voters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    has_voted = Column(Boolean, default=False)

    vote = relationship(
        "Vote",
        back_populates="voter",
        uselist=False,
        cascade="all, delete"
    )