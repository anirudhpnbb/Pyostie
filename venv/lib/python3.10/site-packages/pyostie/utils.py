import os
import shutil
import datetime
import tempfile
from pydub import AudioSegment
from typing import List
from typing import Optional, Callable

extensions = {
    "jpeg": "jpg", 
    "tiff": "jpg", 
    "tif": "jpg", 
    "png": "jpg", 
    "": "txt", 
    "log": "txt", 
    "xls": "xlsx", 
    "mp3": "wav"
}


def process_files(file_list: List[str], output_path: str, folder_name: str) -> None:
    try:
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)

        timestamp = datetime.datetime.today().strftime('%d%m%Y_%H%M') + '_azure_json_processed_files'
        output_dir = os.path.join(output_path, timestamp)
        os.mkdir(output_dir)

        for file in file_list:
            shutil.move(file, output_dir)
        
        shutil.make_archive(output_dir, 'zip', output_path, timestamp)
        shutil.rmtree(output_dir)
    except Exception as ex:
        print(f"An error occurred: {ex}")
        raise


def remove_files(filename_with_path: str) -> None:
    """
    Remove a file if it exists.
    """
    if os.path.isfile(filename_with_path):
        os.remove(filename_with_path)


def remove_folder(foldername_with_path: str) -> None:
    """
    Remove a folder and its contents if it exists.
    """
    if os.path.isdir(foldername_with_path):
        shutil.rmtree(foldername_with_path)


def mp3_to_wav(source: str, dst: str, format: str) -> str:
    sound = AudioSegment.from_mp3(source)
    sound.export(dst, format=format)
    return dst

# Example usage:
# processed_files = process_files(["file1.txt", "file2.jpg"], "/path/to/output", "folder_name")
# remove_files("/path/to/file.txt")
# remove_folder("/path/to/folder")
# mp3_to_wav("source.mp3", "destination.wav", "wav")
