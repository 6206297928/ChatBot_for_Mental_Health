# notebooks/fine_tune_model.py

from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
import torch
from torch.utils.data import Dataset

# --- CONFIG ---
MODEL_NAME = "microsoft/DialoGPT-small"
SAVE_DIR = "../Models/mental_health_model"
EPOCHS = 3
BATCH_SIZE = 2  # keep small for testing
MAX_LEN = 64

# --- DATASET ---
# Tiny example dataset: input -> reply
conversations = [
    {"input": "I feel sad", "reply": "I'm sorry you're feeling sad. Do you want to talk about it?"},
    {"input": "I'm stressed", "reply": "Stress can be tough. Try a deep breath or a short break."},
    {"input": "I feel happy today", "reply": "That's wonderful! What made you feel happy?"},
    {"input": "I am anxious", "reply": "I understand. Take a moment to breathe and calm down."}
]

# --- TOKENIZER AND MODEL ---
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# Make sure padding token exists
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# --- CUSTOM DATASET ---
class ChatDataset(Dataset):
    def __init__(self, conversations, tokenizer, max_len=MAX_LEN):
        self.examples = []
        for c in conversations:
            # Combine input and reply
            text = c["input"] + tokenizer.eos_token + c["reply"] + tokenizer.eos_token
            enc = tokenizer(text, truncation=True, max_length=max_len, padding="max_length")
            self.examples.append(torch.tensor(enc["input_ids"]))
    
    def __len__(self):
        return len(self.examples)
    
    def __getitem__(self, idx):
        input_ids = self.examples[idx]
        # For causal LM, labels = input_ids
        return {"input_ids": input_ids, "labels": input_ids}

dataset = ChatDataset(conversations, tokenizer)

# --- TRAINING ---
training_args = TrainingArguments(
    output_dir=SAVE_DIR,
    num_train_epochs=EPOCHS,
    per_device_train_batch_size=BATCH_SIZE,
    save_steps=500,
    save_total_limit=2,
    logging_steps=10,
    logging_dir="../logs",
    report_to="none",
    remove_unused_columns=False
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset
)

# Train the model
trainer.train()

# Save the fine-tuned model
model.save_pretrained(SAVE_DIR)
tokenizer.save_pretrained(SAVE_DIR)

print("✅ Fine-tuning complete! Model saved at:", SAVE_DIR)
