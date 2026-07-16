import os
import cv2
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_image(frame, question):
    """
    Analyze the current camera frame using Gemini Vision.
    """

    if frame is None:
        return "No camera frame available."

    # Convert OpenCV (BGR) -> RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert to PIL Image
    image = Image.fromarray(rgb)

    prompt = f"""
You are an intelligent AI Vision Assistant.

Analyze ONLY the provided image.

Answer the user's question naturally.

If the answer cannot be determined from the image,
say that you are not sure instead of guessing.

User Question:
{question}
"""

    try:
        response = model.generate_content([prompt, image])

        return response.text

    except Exception as e:
        return f"Vision Error: {e}"