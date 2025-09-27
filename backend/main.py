from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Student Sidekick!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

from backend.routers import qna
app.include_router(qna.router)
