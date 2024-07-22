import os
from pdf2image import convert_from_path
from pyostie.utils import *

class Conversion:

    def __init__(self, filename: str):
        """
        Initialize the Conversion class.

        :param filename: Name of the file to be converted
        """
        self.file = filename

    def convert(self) -> str:
        """
        Convert the PDF file to a JPEG image.

        :return: The filename of the converted image
        """
        if self.file.lower().endswith(".pdf"):
            try:
                pages = convert_from_path(self.file, 500)
                output_filename = self.file[:-4] + '.jpg'
                pages[0].save(output_filename, "JPEG")
                return output_filename
            except Exception as e:
                print(f"An error occurred during conversion: {e}")
                return ""
        else:
            raise ValueError("The file is not a PDF.")

    def remove_file(self, file_to_remove: str):
        """
        Remove the specified file from the filesystem.

        :param file_to_remove: The name of the file to be removed
        """
        try:
            os.remove(file_to_remove)
        except FileNotFoundError:
            print(f"The file {file_to_remove} does not exist.")
        except Exception as e:
            print(f"An error occurred while removing the file: {e}")

# Example usage:
# converter = Conversion("example.pdf")
# jpg_file = converter.convert()
# converter.remove_file(jpg_file)
