from fastapi import APIRouter

router = APIRouter()

@router.get("/quiz/sample")
def sample_quiz():
    return {
        "quiz": [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
            {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"}
        ]
    }
