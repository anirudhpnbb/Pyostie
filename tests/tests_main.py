from os import path
import pytest
import pyostie
from pkgutil import find_loader
from pytesseract import Output

files_path = "test_files/"
expected_columns = [
    'page_num',
    'par_num',
    'line_num',
    'word_num',
    'left',
    'top',
    'width',
    'height',
    'conf',
    'text',
    'image_width',
    'image_height',
    'topLeft',
    'bottomLeft',
    'bottomRight',
    'topRight'
]

pandas_installed = find_loader("pandas") is not None
if pandas_installed:
    import pandas as pd

numpy_installed = find_loader("numpy") is not None
if numpy_installed:
    import numpy as np


def test_placeholder():
    pass


@pytest.fixture(scope='session')
def test_file():
    return path.join(files_path, 'sample.tif')


@pytest.mark.skipif(pandas_installed is False, reason='requires pandas')
def pyostie_dataframe_output(test_file):
    output = pyostie.extract(test_file, insights=True, extension="tif")
    df, text = output.start()
    assert isinstance(df, pd.DataFrame)
    assert bool(set(df.columns).intersection(expected_columns))


@pytest.mark.parametrize(
    'output',
    [Output.STRING, list],
    ids=['string', 'list'],
)
@pytest.mark.skipif(pandas_installed is False, reason="requires pandas")
def pyostie_text_output(test_file, output):
    output1 = pyostie.extract(test_file, insights=False, extension="tif")
    text = output1.start()
    if output == Output.STRING:
        assert isinstance(text, str)
    elif output == list:
        assert isinstance(text, list)
