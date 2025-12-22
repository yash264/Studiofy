import cv2

from models.face_detector import detect_face
from models.deblur import denoise_image
from models.face_enhancer import enhance_face
from processing.background_blur import apply_background_blur
from processing.color_enhance import studio_color_enhance

def run_pipeline(input_path, output_path):
    image = cv2.imread(input_path)

    # 1. Face detection
    face_bbox = detect_face(image)

    # 2. Denoise / deblur
    image = denoise_image(image)

    # 3. Face enhancement
    image = enhance_face(image, face_bbox)

    # 4. Background blur
    image = apply_background_blur(image, face_bbox)

    # 5. Studio color & lighting
    image = studio_color_enhance(image)

    cv2.imwrite(output_path, image)

