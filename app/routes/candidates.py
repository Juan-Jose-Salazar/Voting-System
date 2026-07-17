from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.candidate import CandidateCreate, CandidateResponse
from app.services.candidate_service import CandidateService

router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"]
)

candidate_service = CandidateService()


@router.post(
    "",
    response_model=CandidateResponse,
    status_code=status.HTTP_201_CREATED
)
def create_candidate(
    candidate: CandidateCreate,
    db: Session = Depends(get_db)
):
    return candidate_service.create_candidate(db, candidate)


@router.get(
    "",
    response_model=List[CandidateResponse]
)
def get_candidates(
    db: Session = Depends(get_db)
):
    return candidate_service.get_all_candidates(db)