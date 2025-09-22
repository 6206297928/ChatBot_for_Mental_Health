from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch, random

app = Flask(__name__)

# Load fine-tuned model
MODEL_PATH = "../Models/mental_health_model"
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH)

chat_history_ids = None
last_bot_response = ""

# Backup empathetic responses
fallback_responses = [
    "I hear you. Want to share more?",
    "That sounds tough. How are you coping?",
    "I’m here to listen. Can you tell me a bit more?",
    "It’s okay to feel this way. What do you think would help?",
    "That must be difficult. Do you want to talk about it?"
]

def clean_response(response):
    global last_bot_response

    # Too short or nonsense
    if not response.strip() or len(response.split()) < 2:
        return random.choice(fallback_responses)

    # Repeats last response
    if response.strip().lower() == last_bot_response.strip().lower():
        return random.choice(fallback_responses)

    # Contains junk words
    bad_words = ["kik", "IGN", "Hola!", "old man"]
    if any(bad in response for bad in bad_words):
        return random.choice(fallback_responses)

    # Otherwise return cleaned response
    last_bot_response = response
    return response


def get_bot_response(user_input):
    global chat_history_ids

    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")

    if chat_history_ids is not None:
        bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1)
    else:
        bot_input_ids = new_input_ids

    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.9
    )

    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

    return clean_response(response)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    bot_reply = get_bot_response(user_message)
    return jsonify({"response": bot_reply})


if __name__ == "__main__":
    app.run(debug=True)
