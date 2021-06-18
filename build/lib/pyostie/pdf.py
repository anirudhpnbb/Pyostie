import PyPDF2
import pdfplumber
from pdf2image import convert_from_path
from pkgutil import find_loader


from pyostie.convert import *
from pyostie.insights_ext import *

pandas_installed = find_loader("pandas") is not None
if pandas_installed:
    import pandas as pd


a = pd.DataFrame()
ocr_dict_output = []


class PDFParser:

    def __init__(self, filename, insights=False):
        """

        Parameters
        ----------
        filename : The file that needs to be processed.
        insights : True by default. False if the dataframe is not needed.
        """
        self.file = filename
        self.insights = insights

    def extract_pypdf2(self):
        """

        Returns
        -------
        PDFParser for pdf files.

        """
        contents = []
        text = ' '
        pdfFileObj = open(self.file, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pdfPages = pdfReader.getNumPages()
        if pdfPages == 1:
            for val in range(pdfReader.numPages):
                pageObject = pdfReader.getPage(val)
                text = text + pageObject.extractText()
            contents.append(text)
            if self.insights:
                conv = conversion(self.file)
                __conv = conv.convert()
                insights = generate_insights(__conv, df)
                __insights = insights.generate_df()
                remove_files(__conv)
                return __insights, contents
            else:
                return contents

        if pdfPages >= 2:
            pdf_multipage_df = pd.DataFrame()
            for val in range(pdfReader.numPages):
                pageObject = pdfReader.getPage(val)
                text = text + pageObject.extractText()
            contents.append(text)
            if self.insights:
                df_list = []
                pdffile = self.file
                tempdir = "tempdir"
                if not os.path.isdir(tempdir):
                    os.mkdir(tempdir)
                if os.path.isdir(tempdir):
                    shutil.rmtree(tempdir)
                os.mkdir(tempdir)
                os.mkdir(tempdir + "/converted_files")
                images = convert_from_path(pdffile)
                converted_files = tempdir + "/converted_files/"
                for val in range(len(images)):
                    images[val - 1].save(converted_files + str(val) + ".jpg", "JPEG")
                jpgfiles = os.listdir(converted_files)
                output_files = [converted_files + os.sep + _val for _val in jpgfiles if _val[-3:].upper() == "JPG"]
                for val in range(len(output_files)):
                    insights = generate_insights(output_files[val], df)
                    __insights = insights.generate_df()
                    page = [val] * len(__insights)
                    __insights["page_num"] = page
                    df_list.append(__insights)
                    pdf_multipage_df = pd.concat([pdf_multipage_df, __insights])
                shutil.rmtree(tempdir)
                df1 = pdf_multipage_df.reset_index()
                df1 = df1.drop("index", 1)
                return df1, contents
            else:
                return contents

    def extract_pdfplumber(self):
        """

        Returns
        -------
        Works as an alternative for PyPDF2.
        """
        out_list = []
        with pdfplumber.open(self.file) as pdf:
            for val in range(len(pdf.pages)):
                page = pdf.pages[val]
                output = page.extract_text()
                out_list.append(output)
        return out_list
