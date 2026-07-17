import time
import threading
import cv2

from app.detector import detect


class Camera:

    def __init__(self, assistant, source):

        self.assistant = assistant
        self.source = source

        self.latest_frame = None
        self.latest_objects = []

        self.running = False

        self.lock = threading.Lock()

        self.prev_time = time.time()
        self.fps = 0

        # Turn off if you're using opencv-headless
        self.show_preview = True

    def draw_overlay(self, frame):

        h, w = frame.shape[:2]

        # -------- Grid --------

        rows = 4
        cols = 4

        for i in range(1, cols):
            x = int(w * i / cols)
            cv2.line(frame, (x, 0), (x, h), (60, 60, 60), 1)

        for i in range(1, rows):
            y = int(h * i / rows)
            cv2.line(frame, (0, y), (w, y), (60, 60, 60), 1)

        # -------- Border --------

        cv2.rectangle(
            frame,
            (0, 0),
            (w - 1, h - 1),
            (0, 255, 0),
            2,
        )

        # -------- FPS --------

        current = time.time()

        self.fps = 1 / (current - self.prev_time)

        self.prev_time = current

        # -------- Window Title --------

        title = "Unknown"

        if hasattr(self.source, "window") and self.source.window:

            title = self.source.window.title

        # -------- Capture Mode --------

        mode = type(self.source).__name__

        # -------- Info Box --------

        info = [
            f"Mode : {mode}",
            f"Window : {title}",
            f"Resolution : {w} x {h}",
            f"FPS : {self.fps:.1f}",
            f"Objects : {len(self.latest_objects)}"
        ]

        y = 30

        for line in info:

            cv2.putText(
                frame,
                line,
                (10, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2,
            )

            y += 25

        return frame

    def start(self):

        self.running = True

        print("✅ Capture Started")
        print("Press Q to quit.\n")

        while self.running:

            frame = self.source.get_frame()

            if frame is None:
                continue

            annotated_frame, objects = detect(frame)

            with self.lock:

                self.latest_frame = frame.copy()
                self.latest_objects = objects

            self.assistant.update_objects(objects)

            annotated_frame = self.draw_overlay(annotated_frame)

            if self.show_preview:

                try:
                    cv2.imshow(
                        "AI Video Assistant",
                        annotated_frame
                    )

                    if cv2.waitKey(1) & 0xFF == ord("q"):
                        self.stop()

                except cv2.error:
                    pass

    def stop(self):

        self.running = False

        if self.source:
            self.source.release()

        try:
            cv2.destroyAllWindows()
        except:
            pass

    def get_latest_frame(self):

        with self.lock:

            if self.latest_frame is None:
                return None

            return self.latest_frame.copy()

    def get_latest_objects(self):

        with self.lock:
            return self.latest_objects.copy()

    def save_current_frame(
        self,
        filename="current_frame.jpg"
    ):

        frame = self.get_latest_frame()

        if frame is None:
            return None

        cv2.imwrite(filename, frame)

        return filename