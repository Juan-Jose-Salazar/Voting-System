from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.voter import VoterCreate, VoterResponse
from app.services.voter_service import VoterService

router = APIRouter(
    prefix="/voters",
    tags=["Voters"]
)

voter_service = VoterService()


@router.post(
    "",
    response_model=VoterResponse,
    status_code=status.HTTP_201_CREATED
)
def create_voter(
    voter: VoterCreate,
    db: Session = Depends(get_db)
):
    return voter_service.create_voter(db, voter)


@router.delete(
    "/{voter_id}",
    status_code=status.HTTP_200_OK
)
def delete_voter(
    voter_id: int,
    db: Session = Depends(get_db)
):
    return voter_service.delete_voter(db, voter_id)