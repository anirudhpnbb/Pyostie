import os
import shutil
import datetime
import tempfile
import pytest
import pyostie
from importlib.util import find_spec
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

# Conditional imports for pandas and numpy
pd = pytest.importorskip("pandas")
np = pytest.importorskip("numpy")

def test_placeholder():
    pass

@pytest.fixture(scope='session')
def test_file() -> str:
    return os.path.join(files_path, 'sample.tif')

@pytest.mark.skipif(find_spec("pandas") is None, reason='requires pandas')
def test_pyostie_dataframe_output(test_file: str) -> None:
    output = pyostie.Extract(test_file, insights=True, extension="tif")
    df, text = output.start()
    assert isinstance(df, pd.DataFrame)
    assert bool(set(df.columns).intersection(expected_columns)), "Expected columns not found in DataFrame"

@pytest.mark.parametrize(
    'output',
    [Output.STRING, list],
    ids=['string', 'list'],
)
@pytest.mark.skipif(find_spec("pandas") is None, reason="requires pandas")
def test_pyostie_text_output(test_file: str, output: type) -> None:
    output1 = pyostie.Extract(test_file, insights=False, extension="tif")
    text = output1.start()
    if output == Output.STRING:
        assert isinstance(text, str), "Output is not of type str"