import cv2


class WebcamCapture:

    def __init__(self, camera_index=0):

        self.cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)

        if not self.cap.isOpened():
            raise Exception("❌ Cannot open webcam")

    def get_frame(self):

        ret, frame = self.cap.read()

        if not ret:
            return None

        return frame

    def release(self):

        if self.cap.isOpened():
            self.cap.release()