import unittest
import pyostie
import pandas as pd
from pandas.util.testing import assert_frame_equal


class ImageInsightTest(unittest.TestCase):
    def Insighttest(self):
        output1 = pyostie.extract("sample.tif", insights=True, extension="tif")
        df, text = output1.start()

        df1 = pd.read_excel("sample.xlsx")

        assert_frame_equal(df, df1)


suite = unittest.TestLoader().loadTestsFromTestCase(ImageInsightTest)
unittest.TextTestRunner(verbosity=2).run(suite)