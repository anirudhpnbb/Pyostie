import pytesseract
from pytesseract import Output
import cv2
import pandas as pd
import numpy as np
from PIL import Image

data = pd.DataFrame()

class GenerateInsights:

    def __init__(self, filename: str, data: pd.DataFrame):
        """
        Initialize the GenerateInsights class.

        :param filename: Input the filename as string.
        :param data: Input an empty DataFrame.
        """
        self.file = filename
        self.data = data

    def generate_df(self) -> pd.DataFrame:
        """
        Generate insights and return a DataFrame with text and position data.

        :return: DataFrame with OCR data and image dimensions.
        """
        img = cv2.imread(self.file)
        image = Image.open(self.file)
        w, h = image.size

        # Extract OCR data
        d = pytesseract.image_to_data(img, output_type=Output.DICT)

        # Update DataFrame with OCR data
        self.data = self.data.assign(**d).replace(["", " "], np.NaN).dropna(subset=["text"]).reset_index(drop=True)
        self.data = self.data.drop(columns=["block_num", "level"])

        # Add image dimensions and confidence score
        self.data["conf"] = self.data["conf"] / 100
        self.data["image_width"] = w
        self.data["image_height"] = h

        # Calculate bounding box coordinates
        self.data["top_plus_height"] = self.data["top"] + self.data["height"]
        self.data["left_plus_width"] = self.data["left"] + self.data["width"]

        # Generate corner coordinates
        self.data['topLeft'] = self.data[['left', 'top']].apply(lambda x: f"{x[0]},{x[1]}", axis=1)
        self.data['bottomLeft'] = self.data[['left', 'top_plus_height']].apply(lambda x: f"{x[0]},{x[1]}", axis=1)
        self.data['bottomRight'] = self.data[['left_plus_width', 'top_plus_height']].apply(lambda x: f"{x[0]},{x[1]}", axis=1)
        self.data['topRight'] = self.data[['left_plus_width', 'top']].apply(lambda x: f"{x[0]},{x[1]}", axis=1)

        # Drop intermediate calculation columns
        self.data = self.data.drop(columns=["left_plus_width", "top_plus_height"])

        return self.data

# Example usage:
# df = pd.DataFrame()
# insights = GenerateInsights("example_image.png", df)
# df = insights.generate_df()
