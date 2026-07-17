import cv2
from ocr.reader import OCRReader

image = cv2.imread("current_frame.jpg")

if image is None:
    print("Image not found!")
    exit()

ocr = OCRReader()

text = ocr.read(image)

print("=" * 50)
print(text if text else "No text detected.")
print("=" * 50)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()