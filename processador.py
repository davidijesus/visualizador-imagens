import cv2
import numpy as np

def to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def invert_colors(image):
    return cv2.bitwise_not(image)

def increase_contrast(image):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    return cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

def blur_image(image, ksize=5):
    return cv2.GaussianBlur(image, (ksize, ksize), 0)

def sharpen_image(image):
    kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)

def detect_edges(image):
    gray = to_grayscale(image)
    return cv2.Canny(gray, 100, 200)
