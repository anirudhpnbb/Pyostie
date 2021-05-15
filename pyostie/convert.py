from pdf2image import convert_from_path
from pyostie.utils import *


class conversion:

    def __init__(self, filename):
        """

        Parameters
        ----------
        filename : The file that needs to be processed.
        """
        self.file = filename

    def convert(self):
        """

        Returns
        -------
        Converts a single page pdf file to image and proceeds to process further.
        """
        if self.file[-3::].upper() == "PDF":
            pages = convert_from_path(self.file, 500)
            pages[0].save(self.file[:-4] + '.jpg', "JPEG")
        return self.file[:-4] + ".jpg"

    def remove_file(self, file_to_remove):
        os.remove(file_to_remove)

