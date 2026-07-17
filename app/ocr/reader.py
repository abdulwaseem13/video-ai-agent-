import cv2
import easyocr


class OCRReader:

    def __init__(self):
        self.reader = easyocr.Reader(['en'], gpu=False)

    def read(self, frame):

        if frame is None:
            return ""

        results = self.reader.readtext(frame)

        text = []

        for _, txt, conf in results:
            if conf > 0.3:
                text.append(txt)

        return "\n".join(text)