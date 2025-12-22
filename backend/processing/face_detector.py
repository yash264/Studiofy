import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


MODEL_PATH = "models/blaze_face_short_range.tflite"
base_options = python.BaseOptions(model_asset_path=MODEL_PATH)


options = vision.FaceDetectorOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.IMAGE,
    min_detection_confidence=0.6
)

face_detector = vision.FaceDetector.create_from_options(options)


def detect_face(image):
    h, w, _ = image.shape

    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    result = face_detector.detect(mp_image)

    if not result.detections:
        return None

    detection = result.detections[0]
    bbox = detection.bounding_box

    x = int(bbox.origin_x)
    y = int(bbox.origin_y)
    bw = int(bbox.width)
    bh = int(bbox.height)

    return (x, y, bw, bh)




