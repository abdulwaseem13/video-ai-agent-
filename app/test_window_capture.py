import cv2

from capture.window import WindowCapture


capture = WindowCapture()

capture.select_window()

print("\nPress Q to quit.")

while True:

    frame = capture.get_frame()

    if frame is None:
        continue

    cv2.imshow("Selected Window", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

capture.release()

cv2.destroyAllWindows()