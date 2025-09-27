from fastapi import APIRouter

router = APIRouter()

@router.get("/qna/sample")
def sample_qna():
    return {
        "question": "What is gravity?",
        "answer": "Gravity is a force that attracts objects toward each other."
    }
