import cv2
import numpy as np
from config import BACKGROUND_BLUR_KERNEL

def apply_background_blur(image, bbox):
    if bbox is None:
        return image

    h, w = image.shape[:2]
    mask = np.zeros((h, w), dtype="uint8")

    x, y, bw, bh = bbox
    cv2.rectangle(mask, (x, y), (x + bw, y + bh), 255, -1)

    # Feather mask
    mask = cv2.GaussianBlur(mask, (51, 51), 0)

    blurred = cv2.GaussianBlur(image, BACKGROUND_BLUR_KERNEL, 0)

    mask = mask.astype(float) / 255
    mask = cv2.merge([mask, mask, mask])

    return (image * mask + blurred * (1 - mask)).astype("uint8")

