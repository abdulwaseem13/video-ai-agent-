import cv2
from capture.screen import ScreenCapture


capture = ScreenCapture()

print("🖥️ Screen Capture Started")
print("Press Q to quit.")

while True:

    frame = capture.get_frame()

    cv2.imshow("Screen Capture", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()