import re
import random

# ---------------- RESPONSES ----------------

responses = {
    "greeting": [
        "Hello! How can I help you?",
        "Hi there! What would you like to talk about?",
        "Hey! Ask me anything."
    ],

    "weather": [
        "I can't check real weather, but I hope it's a good day!",
        "Looks like a nice day to code!",
        "Weather APIs are expensive 😄 but imagine it's sunny."
    ],

    "study": [
        "Consistency beats talent while studying.",
        "Try Pomodoro technique: 25 min focus, 5 min break.",
        "Understanding > Memorizing."
    ],

    "ai": [
        "AI is about making machines learn patterns from data.",
        "Machine Learning is a subset of AI.",
        "Deep learning is subset of AI"
        "Explainable AI helps humans trust AI decisions."
    ],

    "fallback": [
        "I'm not sure I understood that.",
        "Can you rephrase your question?",
        "Interesting... tell me more."
    ]
}

# ---------------- INTENT RULES ----------------

patterns = {
    "greeting": r"\b(hi|hello|hey|good morning|good evening)\b",
    "weather": r"\b(weather|rain|sunny|temperature|hot|cold)\b",
    "study": r"\b(study|exam|learn|college|subject|homework)\b",
    "ai": r"\b(ai|machine learning|ml|deep learning|chatgpt|model)\b"
}

# ---------------- INTENT DETECTION ----------------

def detect_intent(user_input):
    user_input = user_input.lower()

    for intent, pattern in patterns.items():
        if re.search(pattern, user_input):
            return intent

    return "fallback"

# ---------------- CHAT FUNCTION ----------------

def chatbot():
    print("Chatbot: Hello! Type 'exit' to stop chatting.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! 👋")
            break

        intent = detect_intent(user_input)
        reply = random.choice(responses[intent])

        print("Chatbot:", reply)

# ---------------- RUN ----------------

if __name__ == "__main__":
    chatbot()