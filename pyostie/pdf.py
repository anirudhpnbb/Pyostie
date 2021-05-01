#!usr/bin/env python3.8

import os
import shutil
from tempfile import mkdtemp
from pdf2image import convert_from_path
import pandas as pd
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from pytesseract import Output

ocr_dict_output = []


class conversion:

    def __init__(self, input_list_dict, filename, dataframe):
        """

        :param input_list:
        """
        self.input = input_list_dict
        self.file = filename
        self.data = dataframe

    def convert(self):
        """

        :return:
        """
        pdffile = "/home/anirudhpnbb/Downloads/Patterson Invoice 1.pdf"
        os.mkdir("tempdir")
        tempdir = "tempdir/"
        os.mkdir("tempdir/converted_files")
        print(os.path.isdir(tempdir))
        # print(converted_files)
        images = convert_from_path(pdffile)
        converted_files = tempdir + "converted_files/"
        for val in range(len(images)):
            images[val - 1].save(converted_files + str(val) + ".jpg", "JPEG")
        jpgfiles = os.listdir(converted_files)
        output_files = [converted_files + os.sep + _val for _val in jpgfiles if _val[-3:].upper() == "JPG"]
        for val in output_files:
            data = Image.open(str(val))
            ocr_dict_output.append(pytesseract.image_to_data(data, output_type=Output.DICT))
        for val in range(len(ocr_dict_output)):
            df = pd.DataFrame(ocr_dict_output[val])
            page =  [val]*len(df)
            df["page_num"] = page
            self.data = pd.concat([self.data, df])
        return self.data
