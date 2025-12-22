import cv2
from processing.face_detector import detect_face
from processing.person_detector import detect_person
from processing.deblur import denoise_image
from processing.face_enhancer import enhance_face
from processing.background_blur import apply_realistic_body_blur
from processing.color_enhance import studio_color_enhance

def run_pipeline(input_path, output_path):
    image = cv2.imread(input_path)

    image = denoise_image(image)

    face_bboxes = detect_face(image)
    if face_bboxes is None:
        face_bboxes = []

    if isinstance(face_bboxes, tuple):
        face_bboxes = [face_bboxes]

    for bbox in face_bboxes:
        image = enhance_face(image, bbox)

    body_bbox = detect_person(image)

    image = apply_realistic_body_blur(image, body_bbox)

    image = studio_color_enhance(image)

    cv2.imwrite(output_path, image)


