import os
import shutil
import datetime
import tempfile
import pydub
import re
import nltk

try:
    stopwords = nltk.corpus.stopwords.words('english')
except Exception:
    nltk.download('stopwords')
    stopwords = nltk.corpus.stopwords.words('english')

extensions = {"jpeg": "jpg", "tiff": "jpg", "tif": "jpg", "png": "jpg", "": "txt", "log": "txt", "xls": "xlsx",
              "mp3": "wav"}


def process_files(file_list, output_path, folder_name):
    """

    Parameters
    ----------
    file_list : The list containing all the files.
    output_path : Path to where they need to be moved.
    folder_name : The name of the folder that needs to be created.
    """
    try:
        if os.path.isdir(folder_name):
            x = datetime.datetime.today().strftime('%d%m%Y_%H%M') + '_azure_json_processed_files'
            os.mkdir(output_path + x)
            for i in file_list:
                shutil.move(i, output_path + x)
            shutil.make_archive(output_path + x, 'zip', output_path, x)
            shutil.rmtree(output_path + x)
        elif not os.path.isdir(folder_name):
            os.mkdir(folder_name)
            x = datetime.datetime.today().strftime('%d%m%Y_%H%M') + '_azure_json_processed_files'
            os.mkdir(output_path + x)
            for i in file_list:
                shutil.move(i, output_path + x)
            shutil.make_archive(output_path + x, 'zip', output_path, x)
            shutil.rmtree(output_path + x)
        else:
            print("Please check and try again.")
    except Exception as ex:
        raise ex


def remove_files(filename_with_path):
    """

    Parameters
    ----------
    filename_with_path : The file that needs to be processed.
    """
    if os.path.isfile(filename_with_path):
        os.remove(filename_with_path)


def remove_folder(foldername_with_path):
    """

    Parameters
    ----------
    foldername_with_path : The folder that needs to be processed.
    """
    if os.path.isdir(foldername_with_path):
        shutil.rmtree(foldername_with_path)


def extension_type_check(extension, input_type):
    """

    Parameters
    ----------
    extension : The extension of the file that needs to be processed.
    input_type : The type of the variable extension.

    Returns
    -------
    The extension with uppercase is returned.
    """

    def decorator(function):
        def wrapper(args):
            if isinstance(args, input_type):
                extnsn = extensions.get(extension, extension)
                return extnsn.upper()
            else:
                print("Bad input type.")

        return wrapper

    return decorator


def mp3_to_wav(source, dst, format):
    """

    Parameters
    ----------
    source : The path to the mp3 file.
    dst : The path where the converted file is stored.
    format : The output format that the file is being saved to.

    Returns
    -------
    The destination of the path where the converted file is saved.
    """
    sound = pydub.AudioSegment.from_mp3(source)
    sound.export(dst, format=format)
    return dst


def cleaning_text(text_to_clean):
    """

    Parameters
    ----------
    text_to_clean : The text that needs to be cleaned for the plots. It's just the output of the processed file.

    Returns
    -------
    Cleaned text.
    """
    text = re.sub("(<.*?>)", " ", text_to_clean)  # Removing html tags.
    text = text.strip()  # Stripping the text of leading and trailing spaces.
    text = re.sub("_+", ' ', text)  # Removing the duplicate underscores.
    text = re.sub(" +", ' ', text)  # Removing the duplicate spaces.
    text = text.replace("/", " ")
    text = text.replace(":", " ")
    text = text.replace("(", " ")
    text = text.replace(")", " ")
    text = text.replace(".", " ")
    text = text.replace(",", " ")
    text = text.replace("’", " ")
    text = text.replace("-", " ")
    return text
