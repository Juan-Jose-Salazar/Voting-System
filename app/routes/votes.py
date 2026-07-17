from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.vote import VoteCreate, VoteResponse
from app.services.vote_service import VoteService
from app.schemas.statistics import StatisticsResponse
from app.services.statistics_service import StatisticsService

router = APIRouter(
    prefix="/votes",
    tags=["Votes"]
)

vote_service = VoteService()
statistics_service = StatisticsService()

@router.post(
    "",
    response_model=VoteResponse,
    status_code=status.HTTP_201_CREATED
)
def create_vote(
    vote: VoteCreate,
    db: Session = Depends(get_db)
):
    return vote_service.create_vote(db, vote)


@router.get(
    "",
    response_model=List[VoteResponse]
)
def get_votes(
    db: Session = Depends(get_db)
):
    return vote_service.get_all_votes(db)

@router.get(
    "/statistics",
    response_model=StatisticsResponse,
    status_code=status.HTTP_200_OK
)
def get_statistics(
    db: Session = Depends(get_db)
):
    return statistics_service.get_statistics(db)