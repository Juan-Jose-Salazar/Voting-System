from typing import Optional

from pydantic import BaseModel, ConfigDict


class CandidateBase(BaseModel):
    name: str
    party: Optional[str] = None


class CandidateCreate(CandidateBase):
    pass


class CandidateResponse(CandidateBase):
    id: int
    votes: int

    model_config = ConfigDict(from_attributes=True)