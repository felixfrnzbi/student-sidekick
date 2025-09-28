def answer_question(query: str) -> str:
    query = query.lower()

    if "gravity" in query:
        return "Gravity is a force that attracts objects toward each other."
    elif "photosynthesis" in query:
        return "Photosynthesis is the process by which plants convert sunlight into energy."
    elif "einstein" in query:
        return "Einstein was a physicist known for the theory of relativity."
    else:
        return "I'm still learning. Try asking about gravity, photosynthesis, or Einstein!"