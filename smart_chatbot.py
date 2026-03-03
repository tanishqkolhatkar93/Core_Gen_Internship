import re
import random
import textblob 
from textblob import TextBlob
import tkinter as tk
from tkinter import scrolledtext

# ---------------- RESPONSES ----------------

responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!"],
    "weather": ["I cannot check live weather, but hope it's nice outside!"],
    "study": ["Consistency beats motivation.", "Try focused 25 min study sessions."],
    "ai": ["AI helps machines learn patterns from data.", "Deep learning is subset of ML" ,"Machine learning is subset of AI"],
    "fallback": ["I didn't understand that.", "Can you rephrase?"]
}

# ---------------- MEMORY ----------------

memory = {
    "name": None,
    "last_topic": None
}

# ---------------- INTENT PATTERNS ----------------

patterns = {
    "greeting": r"\b(hi|hello|hey)\b",
    "weather": r"\b(weather|rain|sunny|temperature)\b",
    "study": r"\b(study|exam|college|learn)\b",
    "ai": r"\b(ai|machine learning|ml|chatgpt |deep learning)\b",
    "name": r"\bmy name is (\w+)\b"
}

# ---------------- SENTIMENT ----------------

def detect_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"

# ---------------- INTENT DETECTION ----------------

def detect_intent(user_input):
    user_input = user_input.lower()

    # detect name
    match = re.search(patterns["name"], user_input)
    if match:
        memory["name"] = match.group(1).capitalize()
        return "name"

    for intent, pattern in patterns.items():
        if re.search(pattern, user_input):
            memory["last_topic"] = intent
            return intent

    return "fallback"

# ---------------- RESPONSE ENGINE ----------------

def get_response(user_input):
    intent = detect_intent(user_input)
    sentiment = detect_sentiment(user_input)

    # name handling
    if intent == "name":
        return f"Nice to meet you, {memory['name']}!"

    reply = random.choice(responses.get(intent, responses["fallback"]))

    # sentiment adjustment
    if sentiment == "negative":
        reply += " I hope things get better!"
    elif sentiment == "positive":
        reply += " That's great!"

    # memory usage
    if memory["name"]:
        reply = f"{memory['name']}, {reply}"

    return reply

# ---------------- GUI ----------------

def send_message():
    user_input = entry.get()
    if not user_input.strip():
        return

    chat_area.insert(tk.END, f"You: {user_input}\n")
    response = get_response(user_input)
    chat_area.insert(tk.END, f"Bot: {response}\n\n")

    entry.delete(0, tk.END)

# window
root = tk.Tk()
root.title("Smart Chatbot")

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
chat_area.pack(padx=10, pady=10)

entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack(pady=5)

root.mainloop()