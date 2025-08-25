import os
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Device config
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Path to fine-tuned T5 model directory inside final_code
MODEL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fine_tuned_t5_crossword")

# Load tokenizer and model once
tokenizer = T5Tokenizer.from_pretrained(MODEL_DIR)
model = T5ForConditionalGeneration.from_pretrained(MODEL_DIR).to(device)
model.eval()


def generate_unique_completions(clue, length, num_completions=10, max_length=50):
    """
    Generate top candidate words using fine-tuned T5 model with beam search.
    """
    # Formulate prompt with task
    input_text = f"predict word from clue: {clue} $ length: {length}"
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True).to(device)

    # Beam search generation
    outputs = model.generate(
        **inputs,
        max_length=max_length,
        num_beams=num_completions,
        num_return_sequences=num_completions,
        early_stopping=True
    )
    # Decode predictions
    completions = [tokenizer.decode(o, skip_special_tokens=True).strip() for o in outputs]
    # Ensure uniqueness preserving order
    unique = []
    for c in completions:
        if c not in unique:
            unique.append(c)
        if len(unique) >= num_completions:
            break
    return unique

