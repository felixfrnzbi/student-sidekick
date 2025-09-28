from fastapi import APIRouter

router = APIRouter()

@router.get("/qna/sample")
def sample_qna():
    return {
        "question": "What is gravity?",
        "answer": "Gravity is a force that attracts objects toward each other."
    }

from fastapi import APIRouter, Query
from pydantic import BaseModel

router = APIRouter()

class Question(BaseModel):
    query: str

@router.post("/qna/ask")
def ask_question(question: Question):
    # Placeholder logic
    if "gravity" in question.query.lower():
        return {"answer": "Gravity is a force that attracts objects toward each other."}
    return {"answer": "I'm still learning. Try asking about gravity!"}
