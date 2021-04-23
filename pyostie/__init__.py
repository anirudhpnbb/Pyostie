from pyostie.parsers import *
from pyostie.insights_ext import *
from pyostie.convert import *
from pyostie.utils import *

df = pd.DataFrame()


class extract:

    def __init__(self, filename, insights=False, tess_path=None, extension=None):
        """
        :param filename:
        :param insights:
        :param tess_path:
        :param extension:

        :return:
        """
        self.file = filename
        self.insights = insights
        self.path = tess_path
        self.ext = extension

    # noinspection PyBroadException
    def start(self):
        """

        :return: Main function to start the process.
        """
        @type_check(str)
        def ext_type_check(extnsn):
            return extnsn.upper()
        ext = ext_type_check(self.ext)

        if ext == "PDF":
            if isinstance(self.file, str):
                try:
                    pdf = PDFParser(self.file, insights=self.insights)
                    output = pdf.extract_pypdf2()
                    return output
                except Exception:
                    try:
                        pdf = PDFParser(self.file)
                        output = pdf.extract_pdfplumber()
                        return output
                    except Exception as ex:
                        raise ex

        elif ext == "CSV":
            if isinstance(self.file, str):
                csv_output = CSVParser(self.file)
                output = csv_output.extract_csv()
                return output

        elif ext == "TXT":
            if isinstance(self.file, str):
                txt = TXTParser(self.file)
                output = txt.extract_txt()
                return output

        elif ext == "XLSX":
            if isinstance(self.file, str):
                excel = XLSXParser(self.file)
                output = excel.extract_xlsx()
                return output

        elif ext == "XLS":
            if isinstance(self.file, str):
                excel = XLSParser(self.file)
                output = excel.extract_xls()
                return output

        elif ext == "DOCX":
            if isinstance(self.file, str):
                docx = DOCXParser(self.file)
                output = docx.extract_docx()
                return output

        elif ext == "JPG" or ext == "TIF" or ext == "PNG":
            if self.insights:
                image = generate_insights(self.file, df)
                output_df = image.generate_df()
                image = ImageParser(self.file)
                output = image.extract_image()
                return output_df, output

            elif not self.insights:
                image = ImageParser(self.file)
                output = image.extract_image()
                return output

