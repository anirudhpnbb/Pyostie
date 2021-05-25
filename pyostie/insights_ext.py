import cv2
import pytesseract
from PIL import Image
from pytesseract import Output
from pkgutil import find_loader

pandas_installed = find_loader("pandas") is not None
if pandas_installed:
    import pandas as pd

numpy_installed = find_loader("numpy") is not None
if numpy_installed:
    import numpy as np


df = pd.DataFrame()


class generate_insights:

    def __init__(self, filename, data):
        """

        Parameters
        ----------
        filename : The file that needs to be processed.
        data : Dataframe to process the insights.
        """
        self.file = filename
        self.data = data

    def generate_df(self):
        """

        Returns
        -------
        A dataframe of insights with word coordinates, para num, line num,
         word num, word height, word width, image height, image width etc.,

        """

        print("Fetching insights....")

        top_plus_height = []
        left_plus_width = []
        img = cv2.imread(self.file)
        image = Image.open(self.file)
        w, h = image.size
        d = pytesseract.image_to_data(img, output_type=Output.DICT)
        self.data = self.data.assign(**d)
        self.data.replace("", np.NaN, inplace=True)
        self.data.replace(" ", np.NaN, inplace=True)
        self.data.dropna(subset=["text"], inplace=True)
        self.data = self.data.reset_index()
        self.data = self.data.drop(["index", "block_num", "level"], 1)
        image_width = [w] * len(self.data)
        image_height = [h] * len(self.data)
        self.data["conf"] = [i / 100 for i in self.data["conf"]]
        self.data["image_width"] = image_width
        self.data["image_height"] = image_height
        for val in range(len(self.data)):
            output = self.data["left"][val] + self.data["width"][val]
            left_plus_width.append(output)
        for val in range(len(self.data)):
            output = self.data["top"][val] + self.data["height"][val]
            top_plus_height.append(output)
        self.data["top_plus_height"] = top_plus_height
        self.data["left_plus_width"] = left_plus_width
        self.data['topLeft'] = tuple(self.data[['left', 'top']].
                                     apply(lambda x: ','.join(x.fillna('').map(str)), axis=1))
        self.data['bottomLeft'] = tuple(self.data[['left', 'top_plus_height']].
                                        apply(lambda x: ','.join(x.fillna('').map(str)), axis=1))
        self.data['bottomRight'] = tuple(self.data[['left_plus_width', 'top_plus_height']].
                                         apply(lambda x: ','.join(x.fillna('').map(str)), axis=1))
        self.data['topRight'] = tuple(self.data[['left_plus_width', 'top']].
                                      apply(lambda x: ','.join(x.fillna('').map(str)), axis=1))
        self.data['topLeft'] = self.data['topLeft'].str.strip(',')
        self.data['bottomLeft'] = self.data['bottomLeft'].str.strip(',')
        self.data['bottomRight'] = self.data['bottomRight'].str.strip(',')
        self.data['topRight'] = self.data['topRight'].str.strip(',')
        self.data = self.data.drop(["left_plus_width", "top_plus_height"], 1)

        return self.data

