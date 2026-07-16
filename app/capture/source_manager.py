from capture.webcam import WebcamCapture
from capture.screen import ScreenCapture
from capture.window import WindowCapture


class SourceManager:

    def __init__(self):
        self.source = None

    def select_source(self):

        print("\n" + "=" * 50)
        print("        🤖 AI VIDEO ASSISTANT")
        print("=" * 50)

        print("\nAI: Select Vision Mode\n")
        print("1. 📷 Webcam")
        print("2. 🖥️ Complete Screen")
        print("3. 🪟 Select Window")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            print("\n✅ Webcam Selected\n")
            self.source = WebcamCapture()

        elif choice == "2":

            print("\n✅ Complete Screen Selected\n")
            self.source = ScreenCapture()

        elif choice == "3":

            print("\nAI: Select the required window\n")

            self.source = WindowCapture()
            self.source.select_window()

        else:

            print("\n❌ Invalid choice")
            exit()

        return self.source