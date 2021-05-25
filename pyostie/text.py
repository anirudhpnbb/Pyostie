class TXTParser:
    
    def __init__(self, filename):
        """

        Parameters
        ----------
        filename : The file that needs to be processed.
        """
        self.file = filename

    def extract_txt(self):
        """

        Returns
        -------
        TXTParser for txt, log or no extension files.
        """
        with open(self.file) as file:
            return file.read()