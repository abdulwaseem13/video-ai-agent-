import sounddevice as sd
from scipy.io.wavfile import write


class Microphone:

    def __init__(self, sample_rate=16000, duration=5):
        self.sample_rate = sample_rate
        self.duration = duration

    def record(self, filename="temp_audio.wav"):
        print("\n🎤 Listening... Speak now.")

        audio = sd.rec(
            int(self.duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        write(filename, self.sample_rate, audio)

        print("✅ Recording saved:", filename)

        return filename