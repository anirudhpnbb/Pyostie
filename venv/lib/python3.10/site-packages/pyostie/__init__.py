#pyostie/__init__.py

__version__ = "2.6.3"

from pyostie.parsers import PDFParser, CSVParser, TXTParser, XLSXParser, DOCXParser, PPTXParser, ImageParser, SpeechToText
from pyostie.insights_ext import GenerateInsights, data
from typing import Union, Tuple, Optional, Any, Callable


class Extract:

    def __init__(self, filename: str, insights: bool = False, tess_path: Optional[str] = None, extension: Optional[str] = None, sheet_name: Optional[str] = None):
        """
        Initialize the Extract class.

        :param filename: Name of the file to process
        :param insights: Boolean indicating whether to generate insights
        :param tess_path: Path to Tesseract OCR
        :param extension: File extension type
        :param sheet_name: Sheet name for Excel files
        """
        self.file: str = filename
        self.insights: bool = insights
        self.path: Optional[str] = tess_path
        self.ext: Optional[str] = extension.upper() if extension else None
        self.sheet: Optional[str] = sheet_name

    def start(self) -> Union[Any, Tuple[Any, Any]]:
        """
        Main function to start the process.

        :return: Processed output based on file type
        """
        print("Process started.....")

        process_func = self._get_process_func()
        if process_func:
            return process_func()
        else:
            raise ValueError(f"Unsupported file extension: {self.ext}")

    def _get_process_func(self) -> Optional[Callable[[], Union[Any, Tuple[Any, Any]]]]:
        """
        Map file extensions to their respective processing functions.

        :return: Corresponding processing function
        """
        process_funcs = {
            "PDF": self._process_pdf,
            "CSV": self._process_csv,
            "TXT": self._process_txt,
            "XLSX": self._process_xlsx,
            "DOCX": self._process_docx,
            "PPTX": self._process_pptx,
            "WAV": self._process_wav,
            "JPG": self._process_image,
            "PNG": self._process_image,
            "TIF": self._process_image,
        }
        return process_funcs.get(self.ext)

    def _process_pdf(self) -> Union[Any, Tuple[Any, Any]]:
        print("PDF file found.....")
        print("Processing the PDF file.....")
        parser = PDFParser(self.file, insights=self.insights)
        try:
            return parser.extract_pypdf2() if not self.insights else parser.extract_pypdf2()
        except Exception:
            return parser.extract_pdfplumber() if not self.insights else parser.extract_pdfplumber()

    def _process_csv(self) -> Any:
        parser = CSVParser(self.file)
        return parser.extract_csv()

    def _process_txt(self) -> Any:
        parser = TXTParser(self.file)
        return parser.extract_txt()

    def _process_xlsx(self) -> Any:
        parser = XLSXParser(filename=self.file, sheet_name=self.sheet)
        return parser.extract_xlsx()

    def _process_docx(self) -> Any:
        parser = DOCXParser(self.file)
        return parser.extract_docx()

    def _process_pptx(self) -> Any:
        parser = PPTXParser(self.file)
        return parser.extract_pptx()

    def _process_wav(self) -> Any:
        parser = SpeechToText(self.file)
        return parser.extract_audio()

    def _process_image(self) -> Union[Any, Tuple[Any, Any]]:
        self.data = data
        if self.insights:
            insights = GenerateInsights(self.file, self.data)
            output_df = insights.generate_df()
            parser = ImageParser(self.file)
            output = parser.extract_image()
            return output_df, output
        else:
            parser = ImageParser(self.file)
            return parser.extract_image()
