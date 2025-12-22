import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "outputs")

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

FACE_ENHANCE_STRENGTH = 0.8
BACKGROUND_BLUR_KERNEL = (35, 35)
