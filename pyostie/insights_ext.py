import pytesseract
from pytesseract import Output
import cv2
import pandas as pd
import numpy as np
from PIL import Image


top_plus_height = []
left_plus_width = []


class generate_insights:

    def __init__(self, filename):
        """

        :param filename:
        """
        self.file = filename

    def generate_df(self):
        """

        :return:
        """
        img = cv2.imread(self.file)
        image = Image.open(self.file)
        w, h = image.size
        d = pytesseract.image_to_data(img, output_type=Output.DICT)
        df = pd.DataFrame(d)
        df.replace("", np.NaN, inplace=True)
        df.replace(" ", np.NaN, inplace=True)
        df.dropna(subset=["text"], inplace=True)
        df = df.reset_index()
        df = df.drop(["index", "block_num", "level"], 1)
        image_width = [w] * len(df)
        image_height = [h] * len(df)
        df["conf"] = [i / 100 for i in df["conf"]]
        df["image_width"] = image_width
        df["image_height"] = image_height
        for val in range(len(df)):
            output = df["left"][val] + df["width"][val]
            left_plus_width.append(output)
        for val in range(len(df)):
            output = df["top"][val] + df["height"][val]
            top_plus_height.append(output)
        df["top_plus_height"] = top_plus_height
        df["left_plus_width"] = left_plus_width
        df['topLeft'] = tuple(df[['left', 'top']].apply(lambda x: ','.join(x.fillna('').map(str)), axis=1))
        df['bottomLeft'] = tuple(df[['left', 'top_plus_height']].apply(lambda x: ','.join(x.fillna('').map(str)), axis=1))
        df['bottomRight'] = tuple(
            df[['left_plus_width', 'top_plus_height']].apply(lambda x: ','.join(x.fillna('').map(str)), axis=1))
        df['topRight'] = tuple(df[['left_plus_width', 'top']].apply(lambda x: ','.join(x.fillna('').map(str)), axis=1))
        df['topLeft'] = df['topLeft'].str.strip(',')
        df['bottomLeft'] = df['bottomLeft'].str.strip(',')
        df['bottomRight'] = df['bottomRight'].str.strip(',')
        df['topRight'] = df['topRight'].str.strip(',')
        df = df.drop(["left_plus_width", "top_plus_height"], 1)
        return df
