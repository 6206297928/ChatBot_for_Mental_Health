# 🧠 Mental Health Chatbot  

A simple **AI-powered chatbot** built with **Flask** and **Hugging Face Transformers** that provides empathetic mental health support.  
This chatbot is not a replacement for professional help, but rather a safe space to talk about emotions.  

---

## 🚀 Features
- Conversational AI using **DialoGPT-small** (fine-tuned for mental health support).  
- Flask backend with REST API.  
- Web UI using HTML/CSS/JS.  
- Stores conversation history (`logs/chat_history.csv`).  
- Filters out irrelevant or unsafe responses.  
- Provides diverse empathetic fallback responses.  

---

## 📂 Project Structure
Mental_Health_Chatbot/
│── app/
│   ├── flask_app.py         # Flask backend
│   ├── templates/
│   │   └── index.html       # Chat UI
│   └── streamlit_app.py     # (Optional) Streamlit UI
│
│── src/
│   ├── chatbot.py           # Chatbot logic
│   ├── utils.py             # Logging and helper functions
│   ├── filters.py           # Offensive content filter
│   └── sentiment.py         # Basic sentiment analyzer
│
│── Models/
│   └── mental_health_model/ # Fine-tuned model (DialoGPT-small)
│
│── notebooks/
│   └── fine_tune_model.py   # Fine-tuning script
│
│── logs/
│   └── chat_history.csv     # Chat history logs
│
│── Data/
│   └── sample_intents.json  # Example dataset
│
│── README.md
│── requirements.txt



---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Mental_Health_Chatbot.git
cd Mental_Health_Chatbot

conda create -n chatbot python=3.10 -y
conda activate chatbot

pip install -r requirements.txt

### Running the chatbot
cd app
python flask_app.py

#Example usage

Bot: Hello! I’m here to chat with you. How are you feeling today?
User: hi
Bot: I’m glad you’re here. What’s on your mind?
User: I’m sad
Bot: I’m sorry you’re feeling this way. Do you want to talk about it?
User: yes
Bot: How has your day been so far?

#Fine tunning the model
Prepare your dataset (sample_intents.json).
python notebooks/fine_tune_model.py

⚠️ Safety Disclaimer

This chatbot is only for educational and supportive conversation purposes.
It is not a replacement for professional therapy or counseling.

If you are in crisis:

Call your local emergency number immediately.

In India: Call 9152987821 (Vandrevala Foundation Helpline).

In the US: Dial 988 (Suicide & Crisis Lifeline).


🚀 Future Improvements

Sentiment-based dynamic responses

Multi-language support

Deployment on Render/Heroku/Replit

Voice-based chat


