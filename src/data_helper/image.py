import base64
import io

import cv2
import numpy as np
import numpy.typing as npt

from PIL import Image, ImageOps


def array2bytes(array: npt) -> bytes:
    """Convert a numpy array to bytes"""
    return array.tobytes()


def bytes2array(byte: bytes, dtype: str = "uint64") -> npt:
    """Convert a byte stream into a numpy array"""
    return np.frombuffer(byte, dtype=dtype)


def pil2cv2(pil: Image):
    pil_image = pil.convert("RGB")
    cv_image = np.array(pil_image, dtype=np.uint8)
    # Convert RGB to BGR
    cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)
    return cv_image


def cv22pil(image, color_format: str = ""):
    # Convert the color format (if needed)
    if color_format.lower() == "bgr":
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    elif color_format.lower() == "hsv":
        image = cv2.cvtColor(image, cv2.COLOR_HSV2RGB)
    elif color_format.lower() == "lab":
        image = cv2.cvtColor(image, cv2.COLOR_LAB2RGB)
    # Create a PIL image from the numpy array
    im_pil = Image.fromarray(image)
    return im_pil


def pil2bytes(pil: Image) -> bytes:
    """Convert a numpy array to bytes"""
    img_bytes = io.BytesIO()
    pil.save(img_bytes, format="JPEG", quality=100, subsampling=0)
    return img_bytes.getvalue()


def bytes2pil(bytes_data, using_index=22, is_flip=True):
    if using_index > 0:
        bytes_data = bytes_data[using_index:]

    image = Image.open(io.BytesIO(base64.b64decode(bytes_data)))
    if is_flip:
        image = ImageOps.mirror(image)
    image_new = Image.new("RGB", image.size, (255, 255, 255))
    image_new.paste(image, mask=image.split()[3])

    return image_new


def cv22bytes(image: npt.NDArray[np.uint8]) -> bytes:
    return cv2.imencode(
        ".jpg",
        image,
        [cv2.IMWRITE_JPEG_QUALITY, 100, cv2.IMWRITE_JPEG_SAMPLING_FACTOR, cv2.IMWRITE_JPEG_SAMPLING_FACTOR_444],
    )[1].tobytes()


def bytes2cv2(bytes_data, using_index=22, is_flip=True):
    pil_image = bytes2pil(bytes_data, using_index, is_flip)
    return pil2cv2(pil_image)
