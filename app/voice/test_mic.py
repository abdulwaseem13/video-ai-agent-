from app.voice.microphone import Microphone
# from microphone import Microphone

mic = Microphone(duration=5)

audio_file = mic.record()

print("Saved:", audio_file)