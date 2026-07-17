import cv2
import threading
from detector import detect


class Camera:

    def __init__(self, assistant, source):

        self.assistant = assistant
        self.source = source

        self.latest_frame = None
        self.latest_objects = []

        self.running = False

        self.lock = threading.Lock()

    def start(self):

        self.running = True

        print("✅ Capture Started")
        print("Press 'Q' to quit.\n")

        while self.running:

            frame = self.source.get_frame()

            if frame is None:
                continue

            annotated_frame, objects = detect(frame)

            with self.lock:

                self.latest_frame = frame.copy()
                self.latest_objects = objects

            self.assistant.update_objects(objects)

            cv2.imshow("Video AI Assistant", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                self.stop()

    def stop(self):

        self.running = False

        if self.source is not None:
            self.source.release()

        cv2.destroyAllWindows()

    def get_latest_frame(self):

        with self.lock:

            if self.latest_frame is None:
                return None

            return self.latest_frame.copy()

    def get_latest_objects(self):

        with self.lock:
            return self.latest_objects.copy()

    def save_current_frame(self, filename="current_frame.jpg"):

        frame = self.get_latest_frame()

        if frame is None:
            return None

        cv2.imwrite(filename, frame)

        return filename