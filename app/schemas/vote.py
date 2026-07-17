from pydantic import BaseModel, ConfigDict


class VoteBase(BaseModel):
    voter_id: int
    candidate_id: int


class VoteCreate(VoteBase):
    pass


class VoteResponse(VoteBase):
    id: int

    model_config = ConfigDict(from_attributes=True)