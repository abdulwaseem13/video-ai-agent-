from pathlib import Path
from ultralytics import YOLO

MODEL_PATH = Path(__file__).parent.parent / "models" / "yolov8n.pt"

model = YOLO(str(MODEL_PATH))

def analyze_frame(frame):
    results = model(frame, verbose=False)

    objects = []

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            confidence = float(box.conf[0])

            objects.append({
                "name": class_name,
                "confidence": round(confidence, 2)
            })

    return objects
