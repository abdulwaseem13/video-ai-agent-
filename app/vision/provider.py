from vision.gemini_provider import GeminiProvider


class VisionProvider:

    def __init__(self):

        self.provider = GeminiProvider()

        # Later:
        # self.provider = OpenRouterProvider()

    def analyze(self, frame, question):

        return self.provider.analyze(
            frame,
            question
        )