from app.voice.microphone import Microphone
from app.voice.speech_to_text import SpeechToText

mic = Microphone(duration=5)
stt = SpeechToText()

audio = mic.record()

text = stt.transcribe(audio)

print("\nYou said:")
print(text)