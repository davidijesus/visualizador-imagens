# utils.py
import cv2
import io
from PIL import Image

def load_image(path):
    return cv2.imread(path)

def save_image(image, path):
    cv2.imwrite(path, image)

def convert_cv2_to_bytes(image):
    # Converte uma imagem OpenCV para bytes, para exibição no PySimpleGUI.
    if image is None:
        return None

    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    else:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    img_pil = Image.fromarray(image)
    with io.BytesIO() as buf:
        img_pil.save(buf, format="PNG")
        return buf.getvalue()

