from .microphone import Microphone
from .speech_to_text import SpeechToText
from .text_to_speech import TextToSpeech


class VoiceAssistant:

    def __init__(self):
        self.microphone = Microphone(duration=5)
        self.stt = SpeechToText()
        self.tts = TextToSpeech()

    def listen(self):

        audio_file = self.microphone.record()

        text = self.stt.transcribe(audio_file)

        print(f"\n🎤 You: {text}")

        return text

    def speak(self, response):

        self.tts.speak(response)