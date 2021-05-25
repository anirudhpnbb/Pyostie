import os
import speech_recognition as sr

from pyostie.utils import *


class speech_to_text:
    
    def __init__(self, filename):
        """

        Parameters
        ----------
        filename : The file that needs to be processed.
        """
        self.file = filename

    def extract_audio(self):
        """

        Returns
        -------
        speech_to_text for mp3, wav files.
        """
        output_audio = []
        os.mkdir("tempdir")
        dst_file = mp3_to_wav(self.file, "tempdir/sample.wav", format="wav")
        output = sr.AudioFile(dst_file)
        recog = sr.Recognizer()
        with output as source:
            audio = recog.record(source)
        output_audio.append(recog.recognize_google(audio))
        shutil.rmtree("tempdir")
        return output_audio
