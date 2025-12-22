import cv2
import numpy as np


def apply_realistic_body_blur(image, body_bbox):
    if body_bbox is None:
        return image

    h, w = image.shape[:2]
    x, y, bw, bh = body_bbox

    x = max(0, x)
    y = max(0, y)
    bw = min(bw, w - x)
    bh = min(bh, h - y)

    mask = np.zeros((h, w), dtype=np.float32)
    center = (x + bw // 2, y + bh // 2)
    axes = (int(bw * 0.6), int(bh * 0.8))
    cv2.ellipse(mask, center, axes, 0, 0, 360, 1, -1)
    mask = cv2.GaussianBlur(mask, (41, 41), 0)

    dist_transform = cv2.distanceTransform((mask < 0.5).astype(np.uint8), cv2.DIST_L2, 5)
    depth = dist_transform / dist_transform.max()

    bg_blur_far = cv2.GaussianBlur(image, (45, 45), 0)
    bg_blur_mid = cv2.GaussianBlur(image, (25, 25), 0)

    bg_blur = bg_blur_mid * (1 - depth[..., None]) + bg_blur_far * depth[..., None]

    mask_3c = cv2.merge([mask, mask, mask])
    result = image * mask_3c + bg_blur * (1 - mask_3c)

    return result.astype(np.uint8)



