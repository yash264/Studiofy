import cv2

def studio_color_enhance(image):
    image = cv2.convertScaleAbs(image, alpha=1.15, beta=10)

    # Warm studio tones
    image[:, :, 1] = cv2.add(image[:, :, 1], 5)
    image[:, :, 2] = cv2.add(image[:, :, 2], 10)

    return image
