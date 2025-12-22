import cv2
import numpy as np


def studio_color_enhance(image):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=1.6, tileGridSize=(8, 8))
    l = clahe.apply(l)

    a = np.clip(a + 2, 0, 255).astype(np.uint8)
    b = np.clip(b + 4, 0, 255).astype(np.uint8)

    lab = cv2.merge((l, a, b))
    image = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    gamma = 1.05
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(256)]).astype("uint8")
    image = cv2.LUT(image, table)

    image = cv2.convertScaleAbs(image, alpha=1.05, beta=4)

    return image


