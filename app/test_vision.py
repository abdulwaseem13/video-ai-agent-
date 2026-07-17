from vision.provider import VisionProvider

vision = VisionProvider()

image_path = "C:\\Users\\INFOMERICA-1095\\Pictures\\Screenshots\\Screenshot 2026-07-16 185203.png"   # Replace with your image path

description = vision.describe(image_path)

print("\n==============================")
print("VISION DESCRIPTION")
print("==============================\n")

print(description)