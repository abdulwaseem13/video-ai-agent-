import threading

from assistant import Assistant
from camera import Camera
from capture.source_manager import SourceManager


def main():

    assistant = Assistant()

    # Select capture source
    source = SourceManager().select_source()

    camera = Camera(
        assistant=assistant,
        source=source
    )

    assistant.set_camera(camera)

    camera_thread = threading.Thread(
        target=camera.start,
        daemon=True
    )

    camera_thread.start()

    print("\n===================================")
    print(" Desktop AI Assistant")
    print(" Type 'exit' to quit")
    print("===================================\n")

    while True:

        question = input("You: ").strip()

        if not question:
            continue

        if question.lower() in ["exit", "quit", "stop"]:
            break

        try:
            answer = assistant.ask(question)
            print(f"\nAI: {answer}\n")

        except Exception as e:
            print(f"\nError: {e}\n")

    camera.stop()


if __name__ == "__main__":
    main()