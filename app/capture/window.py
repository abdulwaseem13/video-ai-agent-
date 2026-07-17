import cv2
import mss
import numpy as np
import pygetwindow as gw

import win32gui
import win32ui
import win32con

from ctypes import windll


class WindowCapture:

    def __init__(self):

        self.sct = mss.mss()
        self.window = None
        self.hwnd = None

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

            print(f"{i+1}. {w.title}")

        choice = int(input("\nSelect Window: ")) - 1

        self.window = windows[choice]

        self.hwnd = self.window._hWnd

        print(f"\n✅ Selected: {self.window.title}")

    def _capture_printwindow(self):

        left, top, right, bottom = win32gui.GetClientRect(self.hwnd)

        width = right - left
        height = bottom - top

        hwndDC = win32gui.GetWindowDC(self.hwnd)

        mfcDC = win32ui.CreateDCFromHandle(hwndDC)

        saveDC = mfcDC.CreateCompatibleDC()

        bitmap = win32ui.CreateBitmap()

        bitmap.CreateCompatibleBitmap(mfcDC, width, height)

        saveDC.SelectObject(bitmap)

        result = windll.user32.PrintWindow(
            self.hwnd,
            saveDC.GetSafeHdc(),
            3
        )

        if result != 1:

            win32gui.DeleteObject(bitmap.GetHandle())

            saveDC.DeleteDC()

            mfcDC.DeleteDC()

            win32gui.ReleaseDC(self.hwnd, hwndDC)

            return None

        bmpinfo = bitmap.GetInfo()

        bmpstr = bitmap.GetBitmapBits(True)

        frame = np.frombuffer(
            bmpstr,
            dtype=np.uint8
        )

        frame.shape = (
            bmpinfo["bmHeight"],
            bmpinfo["bmWidth"],
            4
        )

        frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGRA2BGR
        )

        win32gui.DeleteObject(bitmap.GetHandle())

        saveDC.DeleteDC()

        mfcDC.DeleteDC()

        win32gui.ReleaseDC(self.hwnd, hwndDC)

        return frame

    def _capture_mss(self):

        left = self.window.left
        top = self.window.top
        width = self.window.width
        height = self.window.height

        monitor = {
            "left": left,
            "top": top,
            "width": width,
            "height": height
        }

        img = self.sct.grab(monitor)

        frame = np.array(img)

        frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGRA2BGR
        )

        return frame

    def get_frame(self):

        if self.window is None:

            return None

        if self.window.isMinimized:

            return None

        frame = self._capture_printwindow()

        if frame is None:

            frame = self._capture_mss()

        return frame

    def release(self):

        self.sct.close()