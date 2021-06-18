import pytesseract
from PIL import Image


class ImageParser:
    
    def __init__(self, filename, tess_path=None):
        """

        Parameters
        ----------
        filename : The file that needs to be processed.
        tess_path : The path to the tesseract cmd (Only for windows.)
        """
        self.file = filename
        self.path = tess_path

    def extract_image(self):
        """

        Returns
        -------
        ImageParser for Image formats.

        """
        out_list = []
        if self.path is not None:
            pytesseract.pytesseract.tesseract_cmd = self.path
            img = Image.open(self.file)
            text = pytesseract.image_to_string(img)
            out_list.append(text)
        else:
            img = Image.open(self.file)
            text = pytesseract.image_to_string(img)
            out_list.append(text)
        return out_list
