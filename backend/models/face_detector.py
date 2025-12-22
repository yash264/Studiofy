from huggingface_hub import hf_hub_download
from ultralytics import YOLO

# Download once and cache
model_path = hf_hub_download(
    repo_id="arnabdhar/YOLOv8-Face-Detection",
    filename="model.pt"
)

# Load ONCE
model = YOLO(model_path)

def detect_face(image):
    results = model(image, conf=0.6, verbose=False)

    if not results or len(results[0].boxes) == 0:
        return None

    x1, y1, x2, y2 = (
        results[0].boxes.xyxy[0]
        .cpu()
        .numpy()
        .astype(int)
    )

    return (x1, y1, x2 - x1, y2 - y1)


