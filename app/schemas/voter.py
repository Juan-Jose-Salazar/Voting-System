from pydantic import BaseModel, EmailStr, ConfigDict


class VoterBase(BaseModel):
    name: str
    email: EmailStr


class VoterCreate(VoterBase):
    pass


class VoterResponse(VoterBase):
    id: int
    has_voted: bool

    model_config = ConfigDict(from_attributes=True)