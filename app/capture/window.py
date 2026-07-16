import cv2
import mss
import numpy as np
import pygetwindow as gw


class WindowCapture:

    def __init__(self):

        self.sct = mss.mss()

        self.window = None

    def list_windows(self):

        windows = []

        for w in gw.getAllWindows():

            if w.title.strip():

                windows.append(w)

        return windows

    def select_window(self):

        windows = self.list_windows()

        print("\nOpen Windows:\n")

        for i, w in enumerate(windows):

            print(f"{i + 1}. {w.title}")

        choice = int(input("\nSelect Window: ")) - 1

        self.window = windows[choice]

        print(f"\n✅ Selected: {self.window.title}")

    def get_frame(self):

        if self.window is None:
            return None

        if self.window.isMinimized:
            return None

        left = self.window.left
        top = self.window.top
        width = self.window.width
        height = self.window.height

        print(
        f"Capturing: {self.window.title} | "
        f"Left={left}, Top={top}, Width={width}, Height={height}"
        )

        monitor = {
            "left": left,
            "top": top,
            "width": width,
            "height": height,
        }

        

        img = self.sct.grab(monitor)

        frame = np.array(img)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        return frame
    

    def release(self):

        self.sct.close()