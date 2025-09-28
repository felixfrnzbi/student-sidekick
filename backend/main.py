from fastapi import FastAPI
from backend.routers import qna

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Student Sidekick!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(qna.router)

from backend.routers import quiz
app.include_router(quiz.router)
