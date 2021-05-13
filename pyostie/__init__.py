from pyostie.parsers import *
from pyostie.insights_ext import *
from pyostie.convert import *
from pyostie.utils import *
from pyostie.plots import *


class extract:

    def __init__(self, filename, insights=False, tess_path=None, extension=None, plotting=True, figsize=None):
        """
        :param filename:
        :param insights:
        :param tess_path:
        :param extension:
        :param plotting:
        :param figsize:

        :return:
        """
        self.file = filename
        self.insights = insights
        self.path = tess_path
        self.ext = extension
        self.plots = plotting
        self.size = figsize

    # noinspection PyBroadException
    def start(self):
        """

        :return: Main function to start the process.
        """

        @extension_type_check(self.ext, str)
        def ext_type_check(extnsn):
            return extnsn

        ext = ext_type_check(self.ext)
        print(ext)

        if ext.upper() == "PDF":
            if isinstance(self.file, str):
                try:
                    if self.insights:
                        pdf = PDFParser(self.file, insights=self.insights)
                        output_df, output = pdf.extract_pypdf2()
                        return output_df, output
                    else:
                        pdf = PDFParser(self.file, insights=self.insights)
                        output = pdf.extract_pypdf2()
                        return output
                except Exception:
                    try:
                        if self.insights:
                            pdf = PDFParser(self.file)
                            output_df, output = pdf.extract_pdfplumber()
                            return output_df, output
                        else:
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

        elif ext == "DOCX":
            if isinstance(self.file, str):
                docx = DOCXParser(self.file)
                output = docx.extract_docx()
                return output

        elif ext == "JPG":
            if self.insights:
                if self.plots:
                    image = generate_insights(self.file, df)
                    output_df = image.generate_df()
                    image = ImageParser(self.file)
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
                    image = ImageParser(self.file)
                    output = image.extract_image()
                    return output_df, output

            elif not self.insights:
                if self.plots:
                    image = ImageParser(self.file)
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
                    image = ImageParser(self.file)
                    output = image.extract_image()
                    return output

        elif ext == "PPTX":
            pptx = PPTXParser(self.file)
            output = pptx.extract_pptx()
            return output

        elif ext == "WAV":
            wav = speech_to_text(self.file)
            output = wav.extract_audio()
            return output
