import os
import matplotlib
matplotlib.use("Agg")  # Use a non-interactive backend for matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.candidate_repository import CandidateRepository
from app.repositories.voter_repository import VoterRepository
from app.schemas.statistics import (
    CandidateStatistics,
    StatisticsResponse,
)


class StatisticsService:

    def __init__(self):
        self.candidate_repository = CandidateRepository()
        self.voter_repository = VoterRepository()

    def get_statistics(self, db: Session) -> StatisticsResponse:

        try:

            candidates = self.candidate_repository.get_all(db)

            total_votes = sum(
                candidate.votes
                for candidate in candidates
            )

            total_voters_voted = (
                self.voter_repository.count_voters_voted(db)
            )

            statistics = []

            names = []
            votes = []

            for candidate in candidates:

                percentage = (
                    (candidate.votes / total_votes) * 100
                    if total_votes > 0
                    else 0
                )

                statistics.append(
                    CandidateStatistics(
                        candidate=candidate.name,
                        votes=candidate.votes,
                        percentage=round(percentage, 2)
                    )
                )

                names.append(candidate.name)
                votes.append(candidate.votes)

            os.makedirs("charts", exist_ok=True)

            df = pd.DataFrame({
                "Candidate": names,
                "Votes": votes
            })

            plt.figure(figsize=(8, 5))

            plt.bar(
                df["Candidate"],
                df["Votes"]
            )

            plt.title("Votes by Candidate")

            plt.xlabel("Candidates")

            plt.ylabel("Votes")

            plt.tight_layout()

            chart_path = "charts/votes_chart.png"

            plt.savefig(chart_path)

            plt.close()

            return StatisticsResponse(
                total_voters_voted=total_voters_voted,
                total_votes=total_votes,
                candidates=statistics,
                chart_path=chart_path
            )

        except HTTPException:
            raise

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )