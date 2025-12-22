import cv2

def denoise_image(image):
    return cv2.fastNlMeansDenoisingColored(
        image, None, 8, 8, 7, 21
    )

