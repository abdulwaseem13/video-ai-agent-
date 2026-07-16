import cv2
from detector import detect


class Camera:
    def __init__(self, assistant, source):
        """
        assistant : Assistant object
        source    : WebcamCapture / ScreenCapture / WindowCapture
        """
        self.assistant = assistant
        self.source = source

        self.latest_frame = None
        self.running = False

    def start(self):
        self.running = True

        print("✅ Capture Started")
        print("Press 'Q' on the video window to quit.\n")

        while self.running:

            # Get frame from selected source
            frame = self.source.get_frame()

            if frame is None:
                continue

            # Save latest frame
            self.latest_frame = frame.copy()

            # Run YOLO Detection
            annotated_frame, objects = detect(frame)

            # Update assistant with detected objects
            self.assistant.update_objects(objects)

            # Display output
            cv2.imshow("Video AI Assistant", annotated_frame)

            # Exit on Q
            if cv2.waitKey(1) & 0xFF == ord("q"):
                self.stop()

    def stop(self):
        self.running = False

        # Release selected capture source
        if self.source is not None:
            self.source.release()

        cv2.destroyAllWindows()

    def get_latest_frame(self):
        """
        Returns the latest captured frame.
        Used by Vision AI / LLM.
        """
        return self.latest_frame

    def save_current_frame(self, filename="current_frame.jpg"):
        """
        Save the current frame to disk.
        """
        if self.latest_frame is not None:
            cv2.imwrite(filename, self.latest_frame)
            return filename

        return None