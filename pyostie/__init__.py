from pyostie.pdf_parser import *
from pyostie.csv_parser import *
from pyostie.txt_parser import *
from pyostie.xls_parser import *
from pyostie.xlsx_parser import *


class extract:

    def __init__(self, filename, tess_path=None, extension=None):
        """

        :param filename:
        :param input_file_ext:
        :param method:
        :param tess_path:
        :param encoding:
        """
        self.file = filename
        self.path = tess_path
        self.ext = extension

    def start(self):
        """

        :return:
        """
        if self.ext.upper() == "PDF":
            if isinstance(self.file, str):
                try:
                    pdf = PDFParser(self.file)
                    output = pdf.extract_pypdf2()
                    return output
                except Exception:
                    try:
                        pdf = PDFParser(self.file)
                        output = pdf.extract_pdfplumber()
                        return output
                    except Exception as ex:
                        raise ex
        elif self.ext.upper() == "CSV":
            if isinstance(self.file, str):
                csv_output = CSVParser(self.file)
                output = csv_output.extract_csv()
                return output
        elif self.ext.upper() == "TXT":
            if isinstance(self.file, str):
                txt = TXTParser(self.file)
                output = txt.extract_txt()
                return output
        elif self.ext.upper() == "XLSX":
            if isinstance(self.file, str):
                excel = XLSXParser(self.file)
                output = excel.extract_xlsx()
                return output
        elif self.ext.upper() == "XLS":
            if isinstance(self.file, str):
                excel = XLSParser(self.file)
                output = excel.extract_xls()
                return output
