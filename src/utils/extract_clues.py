import os
import base64
from openai import OpenAI

# Hidden API configuration
TOKEN = "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"
ENDPOINT = "https://models.inference.ai.azure.com"
MODEL_NAME = "gpt-4o"

def get_image_data_url(image_file: str, image_format: str) -> str:
    """
    Helper function to converts an image file to a data URL string.

    Args:
        image_file (str): The path to the image file.
        image_format (str): The format of the image file.

    Returns:
        str: The data URL of the image.
    """
    try:
        with open(image_file, "rb") as f:
            image_data = base64.b64encode(f.read()).decode("utf-8")
    except FileNotFoundError:
        raise ValueError(f"Could not read '{image_file}'. Ensure the file exists.")
    return f"data:image/{image_format};base64,{image_data}"


def extract_clues(image_path: str, image_format: str = "jpeg") -> dict:
    """
    Extract crossword clues and their corresponding numbers from an image.

    Args:
        image_path (str): The path to the crossword image.
        image_format (str): The format of the image (default is 'jpeg').

    Returns:
        dict: A JSON object with "across" and "down" clues.
    """
    # Convert the image to a data URL
    image_data_url = get_image_data_url(image_path, image_format)

    # Initialize the OpenAI client
    client = OpenAI(
        base_url=ENDPOINT,
        api_key=TOKEN,
    )

    # Send the image and instructions to the GPT model
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
                            "url": image_data_url,
                            "detail": "high"
                        },
                    },
                ],
            },
        ],
        model=MODEL_NAME,
    )

    # Return the extracted JSON
    return response.choices[0].message.content