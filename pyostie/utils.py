import os
import shutil
import datetime
import tempfile
import pydub

extensions = {"jpeg": "jpg", "tiff":"jpg", "tif": "jpg", "png": "jpg", "":"txt", "log":"txt", "xls": "xlsx", "mp3":"wav"}


def process_files(file_list, output_path, folder_name):
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

    """
    if os.path.isfile(filename_with_path):
        os.remove(filename_with_path)


def remove_folder(foldername_with_path):
    """

    """
    if os.path.isdir(foldername_with_path):
        shutil.rmtree(foldername_with_path)


def extension_type_check(extension, input_type):
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
    sound = pydub.AudioSegment.from_mp3(source)
    sound.export(dst, format=format)
    return dst
