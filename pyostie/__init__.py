from pyostie.csv_extract import *
from pyostie.pdf import *
from pyostie.docx import *
from pyostie.excel import *
from pyostie.image import *
from pyostie.pptx import *
from pyostie.speechtotext import *
from pyostie.text import *
from pyostie.insights_ext import *
from pyostie.convert import *
from pyostie.utils import *
from pyostie.plots import *


class extract:

    def __init__(self, filename, insights=False, tess_path=None, extension=None,
                 plotting=True, figsize=None, img_dir=None, csv_delimiter=","):
        """
        Parameters
        ----------
        filename :  The file that needs to be processed with path.
                    Example:
                        - "path_to_the_file_sample.jpg"
        insights : False by default, True if the user requires the insights dataframe.
        tess_path : Only for windows users, "Path_to_the_tesseract.cmd".
        extension : Extension of the file that needs to be processed.
                    Example:
                        - "jpg", "tif", "txt", "csv", "pdf", "png", "pptx", "xlsx"
        plotting : True by default. False can be given if the user doesn't require the plots.
        figsize : Size of the plot.
                    Example:
                        - (20, 14)
        """
        self.file = filename
        self.insights = insights
        self.path = tess_path
        self.ext = extension
        self.plots = plotting
        self.size = figsize
        self.delimiter = csv_delimiter
        self.img_dir = img_dir

    # noinspection PyBroadException
    def start(self):
        """

        Returns
        -------
         The main function to start the process. Returns a dataframe and a string/list of continuous
        text if insights=True, else if insights=False, only the string/list of text is returned.

        """

        print("Process started....")
        print("_________________________________")

        @extension_type_check(self.ext, str)
        def ext_type_check(extnsn):
            return extnsn

        ext = ext_type_check(self.ext)

        if ext.upper() == "JPG" or ext.upper() == "GIF":
            print("Image file found....")
        elif ext.upper() == "PDF":
            print("PDF file found....")
        elif ext.upper() == "PPTX" or ext.upper() == "DOCX" or ext.upper() == "XLSX":
            print("Office file found....")
        elif ext.upper() == "CSV" or ext.upper() == "TSV" or ext.upper() == "TXT":
            print("ASCII file found....")
        else:
            print("File found....")

        print("_________________________________")

        if ext.upper() == "PDF":
            if isinstance(self.file, str):
                try:
                    if self.insights:
                        if self.plots:
                            pdf = PDFParser(self.file, insights=self.insights)
                            output_df, output = pdf.extract_pypdf2()
                            if isinstance(output, str):
                                plot = draw(output, self.size)
                                plot.WC()
                                plot.count_plot()
                            elif isinstance(output, list):
                                plot = draw(output[0], self.size)
                                plot.WC()
                                plot.count_plot()
                            return output_df, output
                        elif not self.plots:
                            pdf = PDFParser(self.file, insights=self.insights)
                            output_df, output = pdf.extract_pypdf2()
                            return output_df, output
                    elif not self.insights:
                        if self.plots:
                            pdf = PDFParser(self.file, insights=self.insights)
                            output_df, output = pdf.extract_pypdf2()
                            if isinstance(output, str):
                                plot = draw(output, self.size)
                                plot.WC()
                                plot.count_plot()
                            elif isinstance(output, list):
                                plot = draw(output[0], self.size)
                                plot.WC()
                                plot.count_plot()
                            return output_df, output
                        elif not self.plots:
                            pdf = PDFParser(self.file, insights=self.insights)
                            output_df, output = pdf.extract_pypdf2()
                            return output_df, output
                except Exception:
                    try:
                        if self.insights:
                            if self.plots:
                                pdf = PDFParser(self.file)
                                output_df, output = pdf.extract_pdfplumber()
                                if isinstance(output, str):
                                    plot = draw(output, self.size)
                                    plot.WC()
                                    plot.count_plot()
                                elif isinstance(output, list):
                                    plot = draw(output[0], self.size)
                                    plot.WC()
                                    plot.count_plot()
                                return output_df, output
                            elif not self.plots:
                                pdf = PDFParser(self.file)
                                output_df, output = pdf.extract_pdfplumber()
                                return output_df, output
                        elif not self.insights:
                            if self.plots:
                                pdf = PDFParser(self.file)
                                output = pdf.extract_pdfplumber()
                                if isinstance(output, str):
                                    plot = draw(output, self.size)
                                    plot.WC()
                                    plot.count_plot()
                                elif isinstance(output[0], list):
                                    plot = draw(output[0], self.size)
                                    plot.WC()
                                    plot.count_plot()
                                return output
                            elif not self.plots:
                                pdf = PDFParser(self.file)
                                output = pdf.extract_pdfplumber()
                                return output
                    except Exception as ex:
                        raise ex

        elif ext == "CSV":
            if isinstance(self.file, str):
                if self.plots:
                    csv_output = CSVParser(self.file, self.delimiter)
                    output = csv_output.extract_csv()
                    if isinstance(output, str):
                        plot = draw(output, self.size)
                        plot.WC()
                        plot.count_plot()
                    elif isinstance(output, list):
                        plot = draw(output[0], self.size)
                        plot.WC()
                        plot.count_plot()
                    return output
                elif not self.plots:
                    csv_output = CSVParser(self.file, self.delimiter)
                    output = csv_output.extract_csv()
                    return output

        elif ext == "TSV":
            self.delimiter = "\t"
            if isinstance(self.file, str):
                if self.plots:
                    csv_output = CSVParser(self.file, self.delimiter)
                    output = csv_output.extract_csv()
                    if isinstance(output, str):
                        plot = draw(output, self.size)
                        plot.WC()
                        plot.count_plot()
                    elif isinstance(output, list):
                        plot = draw(output[0], self.size)
                        plot.WC()
                        plot.count_plot()
                    return output
                elif not self.plots:
                    csv_output = CSVParser(self.file, self.delimiter)
                    output = csv_output.extract_csv()
                    return output

        elif ext == "TXT":
            if isinstance(self.file, str):
                if self.plots:
                    txt = TXTParser(self.file)
                    output = txt.extract_txt()
                    if isinstance(output, str):
                        plot = draw(output, self.size)
                        plot.WC()
                        plot.count_plot()
                    elif isinstance(output, list):
                        plot = draw(output[0], self.size)
                        plot.WC()
                        plot.count_plot()
                    return output
                elif not self.plots:
                    txt = TXTParser(self.file)
                    output = txt.extract_txt()
                    return output

        elif ext == "XLSX":
            if isinstance(self.file, str):
                if self.plots:
                    excel = XLSXParser(self.file)
                    output = excel.extract_xlsx()
                    if isinstance(output, str):
                        plot = draw(output, self.size)
                        plot.WC()
                        plot.count_plot()
                    elif isinstance(output, list):
                        plot = draw(output[0], self.size)
                        plot.WC()
                        plot.count_plot()
                    return output
                elif not self.plots:
                    excel = XLSXParser(self.file)
                    output = excel.extract_xlsx()
                    return output

        elif ext == "DOCX":
            if isinstance(self.file, str):
                if self.plots:
                    docx = DOCXParser(self.file, self.img_dir)
                    output = docx.extract_docx()
                    if isinstance(output, str):
                        plot = draw(output, self.size)
                        plot.WC()
                        plot.count_plot()
                    elif isinstance(output, list):
                        plot = draw(output[0], self.size)
                        plot.WC()
                        plot.count_plot()
                    return output
                elif not self.plots:
                    docx = DOCXParser(self.file, self.img_dir)
                    output = docx.extract_docx()
                    return output

        elif ext == "JPG":
            if self.insights:
                if self.plots:
                    image = generate_insights(self.file, df)
                    output_df = image.generate_df()
                    image = ImageParser(filename=self.file, tess_path=self.path)
                    output = image.extract_image()
                    if isinstance(output, str):
                        plot = draw(output, self.size)
                        plot.WC()
                        plot.count_plot()
                    elif isinstance(output, list):
                        plot = draw(output[0], self.size)
                        plot.WC()
                        plot.count_plot()
                    return output_df, output
                elif not self.plots:
                    image = generate_insights(self.file, df)
                    output_df = image.generate_df()
                    image = ImageParser(filename=self.file, tess_path=self.path)
                    output = image.extract_image()
                    return output_df, output
            elif not self.insights:
                if not self.plots:
                    image = ImageParser(filename=self.file, tess_path=self.path)
                    output = image.extract_image()
                    return output
                elif self.plots:
                    image = ImageParser(filename=self.file, tess_path=self.path)
                    output = image.extract_image()
                    if isinstance(output, str):
                        plot = draw(output, self.size)
                        plot.WC()
                        plot.count_plot()
                    elif isinstance(output, list):
                        plot = draw(output[0], self.size)
                        plot.WC()
                        plot.count_plot()
                    return output
        elif ext == "GIF":
            if self.insights:
                if self.plots:
                    image = ImageParser(self.file, tess_path=self.path)
                    output = image.extract_image()
                    output_df = pd.DataFrame()
                    if isinstance(output, list):
                        plot = draw(output[0], self.size)
                        plot.WC()
                        plot.count_plot()
                    elif isinstance(output, str):
                        plot = draw(output, self.size)
                        plot.WC()
                        plot.count_plot()
                    return output_df, output
                elif not self.plots:
                    image = ImageParser(self.file, tess_path=self.path)
                    output = image.extract_image()
                    output_df = pd.DataFrame()
                    return output_df, output
            elif not self.insights:
                image = ImageParser(self.file, tess_path=self.path)
                output = image.extract_image()
                return output

            elif not self.insights:
                if self.plots:
                    image = ImageParser(self.file, tess_path=self.path)
                    output = image.extract_image()
                    if isinstance(output, str):
                        plot = draw(output)
                        plot.WC()
                        plot.count_plot()
                    elif isinstance(output, list):
                        plot = draw(output[0])
                        plot.WC()
                        plot.count_plot()
                    return output
                elif not self.plots:
                    image = ImageParser(self.file, tess_path=self.path)
                    output = image.extract_image()
                    return output

        elif ext == "PPTX":
            if self.plots:
                pptx = PPTXParser(self.file)
                output = pptx.extract_pptx()
                if isinstance(output, str):
                    plot = draw(output, self.size)
                    plot.WC()
                    plot.count_plot()
                elif isinstance(output, list):
                    plot = draw(output[0], self.size)
                    plot.WC()
                    plot.count_plot()
                return output
            elif not self.plots:
                pptx = PPTXParser(self.file)
                output = pptx.extract_pptx()

        elif ext == "WAV":
            if self.plots:
                wav = speech_to_text(self.file)
                output = wav.extract_audio()
                if isinstance(output, str):
                    plot = draw(output, self.size)
                    plot.WC()
                    plot.count_plot()
                elif isinstance(output, list):
                    plot = draw(output[0], self.size)
                    plot.WC()
                    plot.count_plot()
                return output
            elif not self.plots:
                wav = speech_to_text(self.file)
                output = wav.extract_audio()
                return output
