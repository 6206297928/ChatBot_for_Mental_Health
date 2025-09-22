import random

# pool of empathetic responses
response_pool = {
    "greeting": [
        "Hello! How are you doing today?",
        "Hi there! How are you feeling right now?",
        "Hey! How’s your day going so far?"
    ],
    "sad": [
        "I’m sorry you’re feeling sad. Do you want to talk about it?",
        "That sounds really tough. I’m here to listen if you’d like to share.",
        "I hear you. Sometimes sharing helps — would you like to?"
    ],
    "happy": [
        "That’s wonderful! What’s making you feel happy today?",
        "I’m glad to hear that! Do you want to share more about it?",
        "That’s great! What’s one thing that brought you joy recently?"
    ],
    "stressed": [
        "Stress can be really overwhelming. What do you think is causing it?",
        "I hear you. Stress happens to everyone sometimes — do you want to talk about it?",
        "That sounds tough. Taking a break might help. Want to share what’s on your mind?"
    ],
    "default": [
        "I hear you. Could you tell me more about that?",
        "Thanks for sharing. How are you feeling about it?",
        "I understand. Do you want to dive deeper into that?"
    ]
}

def detect_intent(user_input: str) -> str:
    text = user_input.lower()
    if any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"
    elif "sad" in text:
        return "sad"
    elif "happy" in text or "good" in text:
        return "happy"
    elif "stress" in text or "tired" in text:
        return "stressed"
    else:
        return "default"

def get_diverse_response(intent: str) -> str:
    if intent in response_pool:
        return random.choice(response_pool[intent])
    return random.choice(response_pool["default"])

def chatbot_reply(user_input: str) -> str:
    intent = detect_intent(user_input)
    response = get_diverse_response(intent)
    return response
