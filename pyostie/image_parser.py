import cv2
import pytesseract
from PIL import Image


class ImageParser:

    def __init__(self, filename, tess_path=None):
        """

        :param filename:
        :param tess_path
        """
        self.file = filename
        self.path = tess_path

    def extract_image(self):
        """

        :return:
        """
        out_list = []
        pytesseract.pytesseract.tesseract_cmd = self.path
        img = Image.open(self.file)
        text = pytesseract.image_to_string(img)
        out_list.append(text)
        return out_list
