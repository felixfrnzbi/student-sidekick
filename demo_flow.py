import requests

BASE_URL = "http://127.0.0.1:8000"

def run_demo():
    print("🎬 Student Sidekick Demo Flow\n")

    # 1. Ask a question
    print("Step 1: Asking a question...")
    qna_response = requests.post(f"{BASE_URL}/qna/ask", json={"query": "Can you explain gravity?"})
    print("QnA Response:", qna_response.json(), "\n")

    # 2. Take a quiz
    print("Step 2: Taking a sample quiz...")
    quiz_response = requests.get(f"{BASE_URL}/quiz/sample")
    print("Quiz Response:", quiz_response.json(), "\n")

    # 3. Get study tips
    print("Step 3: Getting study tips for physics...")
    coach_response = requests.get(f"{BASE_URL}/coach/tips", params={"subject": "physics"})
    print("Coach Response:", coach_response.json(), "\n")

    print("✅ Demo complete — Student Sidekick guided a full learning session!")

if __name__ == "__main__":
    run_demo()