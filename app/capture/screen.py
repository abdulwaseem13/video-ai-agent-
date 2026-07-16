import cv2
import mss
import numpy as np


class ScreenCapture:
    def __init__(self, monitor=1):
        """
        monitor=1 -> Primary monitor
        """
        self.sct = mss.mss()
        self.monitor = self.sct.monitors[monitor]

    def get_frame(self):
        screenshot = self.sct.grab(self.monitor)

        frame = np.array(screenshot)

        # Convert BGRA -> BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        return frame

    def release(self):
        self.sct.close()