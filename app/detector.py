from pathlib import Path
from ultralytics import YOLO

# Load YOLO model
MODEL_PATH = Path(__file__).parent.parent / "models" / "yolov8n.pt"
model = YOLO(str(MODEL_PATH))


def detect(frame):
    # Run YOLO with ByteTrack
    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        verbose=False
    )

    result = results[0]

    # Draw boxes with tracking IDs
    annotated_frame = result.plot()

    objects = []

    if result.boxes is None:
        return annotated_frame, objects

    for box in result.boxes:

        # Ignore detections without a track ID
        if box.id is None:
            continue

        track_id = int(box.id.item())

        class_id = int(box.cls.item())
        class_name = model.names[class_id]

        confidence = float(box.conf.item())

        if confidence < 0.5:
            continue

        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())

        objects.append({
            "id": track_id,
            "name": class_name,
            "confidence": round(confidence, 2),

            "x1": x1,
            "y1": y1,
            "x2": x2,
            "y2": y2,

            "center_x": (x1 + x2) // 2,
            "center_y": (y1 + y2) // 2,

            "width": x2 - x1,
            "height": y2 - y1
        })

    return annotated_frame, objects
    print(f"ID: {track_id}, Object: {class_name}")