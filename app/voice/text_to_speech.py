import pyttsx3


class TextToSpeech:

    def __init__(self):
        self.engine = pyttsx3.init()

        # Speaking speed
        self.engine.setProperty("rate", 170)

        # Volume (0.0 to 1.0)
        self.engine.setProperty("volume", 1.0)

    def speak(self, text):
        print(f"\n🤖 AI: {text}")

        self.engine.say(text)
        self.engine.runAndWait()