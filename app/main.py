import threading

from app.assistant import Assistant
from app.camera import Camera
from capture.source_manager import SourceManager
from voice.voice_assistant import VoiceAssistant


def main():

    assistant = Assistant()

    # Select capture source
    source = SourceManager().select_source()

    camera = Camera(
        assistant=assistant,
        source=source
    )

    assistant.set_camera(camera)

    camera_worker = threading.Thread(
        target=camera.start,
        daemon=True
    )

    camera_worker.start()

    voice = VoiceAssistant()

    print("\n🎤 Voice Assistant Ready")
    print("Say 'exit', 'quit', or 'stop' to close.\n")

    try:

        while True:

            question = voice.listen()

            if not question:
                continue

            if question.lower() in [
                "exit",
                "quit",
                "stop"
            ]:

                voice.speak("Goodbye!")

                break

            answer = assistant.ask(question)

            print(f"\n🤖 AI: {answer}\n")

            voice.speak(answer)

    except KeyboardInterrupt:

        print("\nStopping...")

    finally:

        camera.stop()


if __name__ == "__main__":
    main()