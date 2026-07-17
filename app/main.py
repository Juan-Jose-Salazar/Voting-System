from fastapi import FastAPI

from app.database import Base, engine
from app.models import *

from app.routes.voters import router as voter_router
from app.routes.candidates import router as candidate_router
from app.routes.votes import router as vote_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Voting System API",
    version="1.0.0"
)

app.include_router(voter_router)
app.include_router(candidate_router)
app.include_router(vote_router)


@app.get("/")
def home():
    return {"message": "Voting System API"}