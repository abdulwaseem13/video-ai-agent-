"""
Vision Provider

Acts as a common interface for all Vision Models.

Currently:
    - Gemini

Future:
    - Ollama
    - OpenAI
    - Qwen VL
"""

from vision.gemini_provider import GeminiProvider


class VisionProvider:

    def __init__(self):

        # Current Vision Backend
        self.provider = GeminiProvider()

    def describe(self, image_path):

        return self.provider.describe(image_path)