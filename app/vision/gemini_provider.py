import os
import cv2
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai

from app.vision.prompt import VISION_PROMPT

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


class GeminiProvider:

    def analyze(self, frame, question):

        if frame is None:
            return "No frame available."

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        image = Image.fromarray(rgb)

        prompt = f"""
{VISION_PROMPT}

User Question:

{question}
"""

        try:

            response = model.generate_content(
                [
                    prompt,
                    image
                ]
            )

            return response.text

        except Exception as e:

            print(e)

            return "Unable to analyze the image."