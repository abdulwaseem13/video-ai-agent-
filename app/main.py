import threading

from assistant import Assistant
from camera import Camera
from capture.source_manager import SourceManager
from voice.voice_assistant import VoiceAssistant


assistant = Assistant()

# Ask user which vision source to use
source = SourceManager().select_source()

# Create camera with selected source
camera = Camera(assistant, source)

assistant.set_camera(camera)


def camera_thread():
    camera.start()


thread = threading.Thread(target=camera_thread)
thread.daemon = True
thread.start()

voice = VoiceAssistant()

while True:

    question = voice.listen()

    if question.lower() in ["exit", "quit", "stop"]:
        voice.speak("Goodbye!")
        break

    answer = assistant.ask(question)

    print(f"\n🤖 AI: {answer}")

    voice.speak(answer)