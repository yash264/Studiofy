import cv2
import numpy as np


def enhance_face(image, bbox):
    if bbox is None:
        return image

    x, y, w, h = bbox
    h_img, w_img = image.shape[:2]

    x = max(0, x)
    y = max(0, y)
    w = min(w, w_img - x)
    h = min(h, h_img - y)

    face = image[y:y+h, x:x+w].copy()
    if face.size == 0:
        return image

    smooth = cv2.bilateralFilter(face, d=7, sigmaColor=50, sigmaSpace=50)

    lab = cv2.cvtColor(smooth, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=1.6, tileGridSize=(8, 8))
    l = clahe.apply(l)
    lab = cv2.merge((l, a, b))
    enhanced = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    blur = cv2.GaussianBlur(enhanced, (0, 0), 0.8)
    enhanced = cv2.addWeighted(enhanced, 1.1, blur, -0.1, 0)

    mask = np.zeros((h, w), dtype=np.float32)
    cv2.ellipse(mask, (w//2, h//2), (int(w*0.45), int(h*0.48)), 0, 0, 360, 1, -1)
    mask = cv2.GaussianBlur(mask, (31, 31), 0)
    mask = mask[..., None]

    image[y:y+h, x:x+w] = (enhanced * mask + face * (1 - mask)).astype(np.uint8)
    return image



