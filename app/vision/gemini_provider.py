import os
from dotenv import load_dotenv
import google.generativeai as genai

from vision.prompt import VISION_PROMPT

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


class GeminiProvider:

    def describe(self, image_path):

        try:

            image = genai.upload_file(image_path)

            response = model.generate_content(
                [
                    VISION_PROMPT,
                    image
                ]
            )

            return response.text

        except Exception as e:

            print(f"Vision Error: {e}")

            return "Unable to analyze the image."