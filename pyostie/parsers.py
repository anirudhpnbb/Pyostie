import docx2txt
import xlrd
import csv
import cv2
import pytesseract
from PIL import Image
import os
import PyPDF2
import pdfplumber
from tempfile import mkdtemp


class DOCXParser:

    def __init__(self, filename):
        """

        :param filename:
        """
        self.file = filename

    def extract_docx(self):
        """

        :return:
        """
        output = docx2txt.process(self.file)
        return output


class DOCParser:

    def __init__(self, filename):
        """

        :param filename:
        """
        self.file = filename

    def extract_doc(self):
        """

        :return: Text extracted from doc files
        """
        filechange = self.file + "x"
        print(filechange)
        if not os.path.exists(filechange):
            print("hey3")
            os.system('antiword ' + self.file + ' > ' + filechange)
            with open(filechange) as f:
                text = f.read()
            os.remove(filechange)


class XLSXParser:

    def __init__(self, filename):
        """

        :param filename:
        """
        self.file = filename

    def extract_xlsx(self):
        """

        :return:
        """
        out_list = []
        book = xlrd.open_workbook(self.file)
        for val in range(len(book.sheet_names())):
            sheet = book.sheet_by_index(val)
            for res in range(sheet.nrows):
                output = " " + " ".join(str(val_) for val_ in (sheet.row_values(res)))
                out_list.append(output)
        return out_list


class XLSParser:

    def __init__(self, filename):
        """

        :param filename:
        """
        self.file = filename

    def extract_xls(self):
        """

        :return:
        """
        out_list = []
        book = xlrd.open_workbook(self.file)
        for val in range(len(book.sheet_names())):
            sheet = book.sheet_by_index(val)
            for res in range(sheet.nrows):
                output = " " + " ".join(str(val_) for val_ in (sheet.row_values(res)))
                out_list.append(output)
        return out_list


class CSVParser:

    def __init__(self, filename, delimiter=','):
        """

        :param filename:
        """
        self.file = filename
        self.delimiter = delimiter

    def extract_csv(self):
        """

        :return:
        """
        with open(self.file) as file:
            output = csv.reader(file, delimiter=self.delimiter)
            return ' '.join([' '.join(row) for row in output])


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


class TXTParser:

    def __init__(self, filename):
        """

        :param filename:
        """
        self.file = filename

    def extract_txt(self):
        """

        :return:
        """
        with open(self.file) as file:
            return file.read()
