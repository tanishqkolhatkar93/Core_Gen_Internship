# 🤖 Smart Conversational Chatbot (Python + Tkinter + NLP)

A rule-based conversational chatbot built using **Python**,
**Regex-based intent detection**, **Sentiment Analysis**, and a
**Tkinter GUI interface**.

This project demonstrates fundamental NLP concepts, context memory
handling, and GUI-based interaction --- without using heavy machine
learning frameworks.

------------------------------------------------------------------------

## 🚀 Features

-   ✅ Rule-based Intent Recognition using Regex
-   ✅ Sentiment Detection using TextBlob
-   ✅ Conversation Memory (remembers user name & context)
-   ✅ Multiple Conversation Topics (AI, Study, Weather, Greeting)
-   ✅ Fallback Responses for unknown inputs
-   ✅ Interactive GUI using Tkinter
-   ✅ Lightweight & beginner-friendly implementation

------------------------------------------------------------------------

## 🧠 How It Works

User Input → Intent Detection → Sentiment Analysis → Memory Update →
Response Generation → GUI Output

### 🔹 Intent Recognition

Uses keyword-based regex pattern matching to classify input into: -
Greeting - Weather - Study - AI/Technology - Name introduction

### 🔹 Sentiment Detection

Uses TextBlob polarity score to classify: - Positive - Negative -
Neutral

Responses are adjusted accordingly.

### 🔹 Conversation Memory

Stores: - User name - Last topic discussed

Enables personalized responses like: \> "Tanishq, That's great!"

### 🔹 GUI

Built using Tkinter with: - Scrollable chat window - Input field - Send
button

------------------------------------------------------------------------

## 🖥️ Tech Stack

-   Python 3.x
-   Regex (re module)
-   TextBlob (NLP Sentiment Analysis)
-   Tkinter (GUI)

------------------------------------------------------------------------

## 📦 Installation

1.  Clone the repository:

``` bash
git clone https://github.com/yourusername/smart-chatbot.git
cd smart-chatbot
```

2.  Install dependencies:

``` bash
pip install textblob
python -m textblob.download_corpora
```

3.  Run the application:

``` bash
python smart_chatbot.py
```

------------------------------------------------------------------------

## 💬 Example Conversation

User: Hi my name is Tanishq

Bot: Nice to meet you, Tanishq!

User: I am sad about exams

Bot: Tanishq, Consistency beats motivation. I hope things get better!

------------------------------------------------------------------------

## 📸 Result Screenshot




![Live Demo](https://github.com/user-attachments/assets/938bfc20-4123-44f4-9209-cc72156863fb)


![Chatbot](https://github.com/tanishqkolhatkar93/Core_Gen_Internship/blob/main/Screenshot%202026-03-03%20110245.png)

------------------------------------------------------------------------

## 📂 Project Structure

    smart-chatbot/
    │
    ├── smart_chatbot.py
    ├── README.md
    └── screenshots/
        └── chatbot_result.png

------------------------------------------------------------------------

## 🎯 Skills Demonstrated

-   Natural Language Processing Basics
-   Regex Pattern Matching
-   Sentiment Analysis
-   Context Handling & State Management
-   GUI Development with Tkinter
-   Clean Modular Code Structure

------------------------------------------------------------------------

## 📌 Author

**Tanishq Kolhatkar**\
Integrated M.Tech in Artificial Intelligence

Linkedln  -  https://www.linkedin.com/in/tanishq93/

------------------------------------------------------------------------

⭐ If you like this project, consider giving it a star on GitHub!
