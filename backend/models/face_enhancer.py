import cv2

def enhance_face(image, bbox):
    if bbox is None:
        return image

    x, y, w, h = bbox
    face = image[y:y+h, x:x+w]

    if face.size == 0:
        return image

    # Skin smoothing (natural)
    face = cv2.bilateralFilter(face, 9, 75, 75)

    # Sharpen
    face = cv2.addWeighted(
        face, 1.5,
        cv2.GaussianBlur(face, (0, 0), 1),
        -0.5, 0
    )

    image[y:y+h, x:x+w] = face
    return image

