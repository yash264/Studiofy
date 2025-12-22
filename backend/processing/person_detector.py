import cv2
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
WEIGHTS = os.path.join(BASE_DIR, "models/yolov4-tiny.weights")
CFG = os.path.join(BASE_DIR, "models/yolov4-tiny.cfg")
NAMES = os.path.join(BASE_DIR, "models/coco.names")

net = cv2.dnn.readNetFromDarknet(CFG, WEIGHTS)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


with open(NAMES) as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()]


def detect_person(image, conf_threshold=0.5):
    h, w = image.shape[:2]

    blob = cv2.dnn.blobFromImage(
        image, 1 / 255.0, (416, 416), swapRB=True, crop=False
    )
    net.setInput(blob)
    outputs = net.forward(output_layers)

    best_box = None
    best_conf = 0

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = scores.argmax()
            confidence = scores[class_id]

            if classes[class_id] == "person" and confidence > conf_threshold:
                cx, cy, bw, bh = detection[0:4]
                x = int((cx - bw / 2) * w)
                y = int((cy - bh / 2) * h)
                bw = int(bw * w)
                bh = int(bh * h)

                if confidence > best_conf:
                    best_conf = confidence
                    best_box = (x, y, bw, bh)

    return best_box
