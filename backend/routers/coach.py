from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/coach/tips")
def study_tips(subject: str = Query(..., description="The subject you want tips for")):
    subject = subject.lower()

    if "physics" in subject:
        return {
            "subject": "Physics",
            "tips": [
                "Break problems into smaller steps.",
                "Draw diagrams to visualize forces and motion.",
                "Practice derivations, not just memorization."
            ]
        }
    elif "math" in subject:
        return {
            "subject": "Math",
            "tips": [
                "Work through examples by hand.",
                "Focus on understanding the 'why' behind formulas.",
                "Review mistakes to spot patterns."
            ]
        }
    elif "biology" in subject:
        return {
            "subject": "Biology",
            "tips": [
                "Use flashcards for key terms.",
                "Relate processes to real-life examples.",
                "Sketch diagrams of systems like the cell or heart."
            ]
        }
    else:
        return {
            "subject": subject,
            "tips": [
                "Set a timer for focused study sessions (Pomodoro method).",
                "Summarize what you learned in your own words.",
                "Teach the concept to someone else — it reinforces memory."
            ]
        }