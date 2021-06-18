import docx2txt


class DOCXParser:
    
    def __init__(self, filename, img_dir):
        """

        Parameters
        ----------
        filename : The file that needs to be processed.
        """
        self.file = filename
        self.img_dir = img_dir

    def extract_docx(self):
        """

        Returns
        -------
        DOCXParser for Docx files.
        extract text and write images in img_dir

        """
        output = docx2txt.process(self.file, self.img_dir)
        return output
