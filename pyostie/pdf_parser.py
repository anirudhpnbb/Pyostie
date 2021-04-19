import os
import PyPDF2
import shutil
import pdfplumber
from tempfile import mkdtemp


class PDFParser:
    """

    """

    def __init__(self, filename):
        """

        :param filename:
        """
        self.file = filename

    def extract_pypdf2(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        temp_dir = mkdtemp()
        base = os.path.join(temp_dir, 'conv')
        contents = []
        text = ' '
        pdfFileObj = open(self.file, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        for i in range(pdfReader.numPages):
            pageObject = pdfReader.getPage(i)
            text = text + pageObject.extractText(**kwargs)
        contents.append(text)
        return contents

    def extract_pdfplumber(self):
        """

        :return:
        """
        out_list = []
        with pdfplumber.open(self.file) as pdf:
            for val in range(len(pdf.pages)):
                page = pdf.pages[val]
                output = page.extract_text()
                out_list.append(output)
        return out_list
