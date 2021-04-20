from pyostie.parsers import *
from pyostie.insights import *


class extract:

    def __init__(self, filename, insights=False, tess_path=None, extension=None):
        """

        """
        self.file = filename
        self.insights = insights
        self.path = tess_path
        self.ext = extension

    def start(self):
        """

        :return: Main function to start the process.
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
        elif self.ext.upper() == "DOCX":
            if isinstance(self.file, str):
                docx = DOCXParser(self.file)
                output = docx.extract_docx()
                return output
        elif self.ext.upper() == "DOC":
            print("hey1")
            if isinstance(self.file, str):
                print("hey2")
                try:
                    doc = DOCParser(self.file)
                    output = doc.extract_doc()
                    return output
                except Exception as ex:
                    raise ex
        elif self.ext.upper() == "JPG" or self.ext.upper() == "TIF" or self.ext.upper() == "PNG":
            if self.insights:
                image = generate_insights(self.file)
                output_df = image.generate_df()
                image = ImageParser(self.file)
                output = image.extract_image()
                return output_df, output
            elif not self.insights:
                image = ImageParser(self.file)
                output = image.extract_image()
                return output
