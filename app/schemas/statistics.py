from pydantic import BaseModel


class CandidateStatistics(BaseModel):
    candidate: str
    votes: int
    percentage: float


class StatisticsResponse(BaseModel):
    total_voters_voted: int
    total_votes: int
    candidates: list[CandidateStatistics]
    chart_path: str