import os
import pandas as pd
import csv
import cv2
import pytesseract
from PIL import Image
import pdfplumber
from pptx import Presentation
from pdf2image import convert_from_path
import speech_recognition as sr
from pyostie.convert import *
from pyostie.insights_ext import *
import shutil
from docx import Document  # Replacing docx2txt
from openpyxl import load_workbook  # Replacing xlrd
import fitz  # PyMuPDF


class DOCXParser:
    def __init__(self, filename: str):
        """
        Initialize the DOCXParser class.

        :param filename: Path to the DOCX file.
        """
        self.file = filename

    def extract_docx(self) -> str:
        """
        Extract text from the DOCX file.

        :return: Extracted text.
        """
        doc = Document(self.file)
        output = "\n".join([para.text for para in doc.paragraphs])
        return output


class XLSXParser:
    def __init__(self, filename: str, sheet_name: str = None):
        """
        Initialize the XLSXParser class.

        :param filename: Path to the XLSX file.
        :param sheet_name: Specific sheet name to extract data from.
        """
        self.file = filename
        self.sheet = sheet_name

    def extract_xlsx(self) -> list:
        """
        Extract text from the XLSX file.

        :return: Extracted text as a list of strings.
        """
        out_list = []
        workbook = load_workbook(self.file, data_only=True)
        sheets = [self.sheet] if self.sheet else workbook.sheetnames

        for sheet_name in sheets:
            sheet = workbook[sheet_name]
            for row in sheet.iter_rows(values_only=True):
                output = " ".join(str(val) for val in row if val is not None)
                out_list.append(output)
        return out_list


class CSVParser:
    def __init__(self, filename: str, delimiter: str = ','):
        """
        Initialize the CSVParser class.

        :param filename: Path to the CSV file.
        :param delimiter: Delimiter used in the CSV file.
        """
        self.file = filename
        self.delimiter = delimiter

    def extract_csv(self) -> str:
        """
        Extract text from the CSV file.

        :return: Extracted text as a single string.
        """
        with open(self.file) as file:
            output = csv.reader(file, delimiter=self.delimiter)
            return ' '.join([' '.join(row) for row in output])


class ImageParser:
    def __init__(self, filename: str, tess_path: str = None):
        """
        Initialize the ImageParser class.

        :param filename: Path to the image file.
        :param tess_path: Path to the Tesseract executable.
        """
        self.file = filename
        self.path = tess_path

    def extract_image(self) -> str:
        """
        Extract text from the image file.

        :return: Extracted text.
        """
        if self.path:
            pytesseract.pytesseract.tesseract_cmd = self.path
        img = Image.open(self.file)
        text = pytesseract.image_to_string(img)
        return text


class PDFParser:
    def __init__(self, filename: str, insights: bool = False):
        """
        Initialize the PDFParser class.

        :param filename: Path to the PDF file.
        :param insights: Boolean indicating whether to generate insights.
        """
        self.file = filename
        self.insights = insights

    def extract_pymupdf(self) -> str:
        """
        Extract text from the PDF file using PyMuPDF.

        :return: Extracted text.
        """
        doc = fitz.open(self.file)
        text = ""
        for page in doc:
            text += page.get_text()
        return text

    def extract_pdfplumber(self) -> str:
        """
        Extract text from the PDF file using pdfplumber.

        :return: Extracted text.
        """
        out_list = []
        with pdfplumber.open(self.file) as pdf:
            for page in pdf.pages:
                out_list.append(page.extract_text())
        return ' '.join(out_list)


class TXTParser:
    def __init__(self, filename: str):
        """
        Initialize the TXTParser class.

        :param filename: Path to the TXT file.
        """
        self.file = filename

    def extract_txt(self) -> str:
        """
        Extract text from the TXT file.

        :return: Extracted text.
        """
        with open(self.file) as file:
            return file.read()


class PPTXParser:
    def __init__(self, filename: str):
        """
        Initialize the PPTXParser class.

        :param filename: Path to the PPTX file.
        """
        self.file = filename

    def extract_pptx(self) -> str:
        """
        Extract text from the PPTX file.

        :return: Extracted text.
        """
        text = []
        presentation = Presentation(self.file)
        for slide in presentation.slides:
            for shape in slide.shapes:
                if shape.has_text_frame:
                    for paragraph in shape.text_frame.paragraphs:
                        text.append(paragraph.text.strip())
        return ' '.join(text)


class SpeechToText:
    def __init__(self, filename: str):
        """
        Initialize the SpeechToText class.

        :param filename: Path to the audio file.
        """
        self.file = filename

    def extract_audio(self) -> str:
        """
        Extract text from the audio file.

        :return: Extracted text.
        """
        output_audio = []
        os.mkdir("tempdir")
        dst_file = mp3_to_wav(self.file, "tempdir/sample.wav", format="wav")
        recognizer = sr.Recognizer()
        with sr.AudioFile(dst_file) as source:
            audio = recognizer.record(source)
        output_audio.append(recognizer.recognize_google(audio))
        shutil.rmtree("tempdir")
        return ' '.join(output_audio)
