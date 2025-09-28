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


import re

TOPIC_MAP = {
    "gravity": "Gravity is a force that attracts objects toward each other.",
    "photosynthesis": "Photosynthesis is how plants convert sunlight into energy.",
    "einstein": "Einstein developed the theory of relativity.",
    "newton": "Isaac Newton formulated the laws of motion and universal gravitation.",
    "black hole": "A black hole is a region of space with gravity so strong that nothing can escape it.",
    "dna": "DNA is the molecule that carries genetic instructions in living organisms."
}

def answer_question(query: str) -> str:
    query = query.lower()

    for keyword, answer in TOPIC_MAP.items():
        if re.search(rf"\b{re.escape(keyword)}\b", query):
            return answer

    return "I'm still learning. Try asking about gravity, DNA, or black holes!"