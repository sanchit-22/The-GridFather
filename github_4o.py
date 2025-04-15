import os

TOKEN = os.getenv("GITHUB_TOKEN")
import base64
from openai import OpenAI

endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

def get_image_data_url(image_file: str, image_format: str) -> str:
    try:
        with open(image_file, "rb") as f:
            image_data = base64.b64encode(f.read()).decode("utf-8")
    except FileNotFoundError:
        print(f"Could not read '{image_file}'.")
        exit()
    return f"data:image/{image_format};base64,{image_data}"


client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": """
You are tasked with extracting crossword clues and their corresponding clue numbers from an image of a crossword puzzle. The image contains a grid with numbered cells and a list of clues divided into "Across" and "Down" sections. Your goal is to produce a JSON object with the following structure:

The JSON should have two main keys: "across" and "down".

Under each key, include a sub-object where the keys are the clue numbers (as strings) and the values are the clue text.

Include all clues exactly as they appear in the image, preserving punctuation, capitalization, and special characters.
"""
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": get_image_data_url("test2.jpeg", "jpeg"),
                        "detail": "high"
                    },
                },
            ],
        },
    ],
    model=model_name,
)

print(response.choices[0].message.content)