from transformers import pipeline

# Initialize the Hugging Face pipeline for text generation with a smaller model
description_generator = pipeline("text-generation", model="distilgpt2")

def generate_description(item_name, category, quantity):
    prompt = (
        f"Please write a simple yet detailed description of an inventory item. "
        f"The item is called '{item_name}', it belongs to the '{category}' category, "
        f"and there are {quantity} available. "
        f"Include its purpose, features, and any other relevant details that would inform potential buyers."
    )
    response = description_generator(prompt, max_length=150, num_return_sequences=1)
    return response[0]['generated_text'].strip()
