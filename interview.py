from fastapi import APIRouter
from pydantic import BaseModel
import random

from database import (
    insert_interview,
    get_interviews
)

router = APIRouter()


# =========================
# REQUEST MODEL
# =========================
class ChatRequest(BaseModel):
    resume_id: int
    question: str
    answer: str


# =========================
# START INTERVIEW
# =========================
@router.post("/start-interview")
def start_interview():

    questions = [
        "Explain OOP concepts in Python.",
        "Difference between SQL and NoSQL.",
        "What is React Virtual DOM?"
    ]

    return {
        "questions": questions
    }


# =========================
# CHAT ENDPOINT
# =========================
@router.post("/chat")
def chat(data: ChatRequest):

    # Fake AI scoring logic
    score = random.randint(6, 10)

    feedback_list = [
        "Good answer with clear explanation.",
        "Nice understanding of the concept.",
        "Answer is decent but can be improved.",
        "Well structured response.",
        "Good technical explanation."
    ]

    feedback = random.choice(feedback_list)

    # Save into database
    insert_interview(
        data.resume_id,
        data.question,
        data.answer,
        score,
        feedback
    )

    return {
        "message": "Interview saved",
        "result": {
            "score": score,
            "feedback": feedback
        }
    }


# =========================
# REPORT ENDPOINT
# =========================
@router.get("/report/{resume_id}")
def report(resume_id: int):

    interviews = get_interviews(resume_id)

    if not interviews:

        return {
            "message": "No interviews found"
        }

    total = 0

    strengths = []
    weaknesses = []

    for row in interviews:

        total += row["score"]

        if row["score"] >= 7:

            strengths.append(row["question"])

        else:

            weaknesses.append(row["question"])

    average_score = total / len(interviews)

    return {
        "average_score": round(average_score, 2),
        "strengths": strengths,
        "weaknesses": weaknesses
    }