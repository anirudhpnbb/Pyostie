class TXTParser:

    def __init__(self, filename):
        """

        :param filename:
        """
        self.file = filename

    def extract_txt(self):
        """

        :return:
        """
        with open(self.file) as file:
            return file.read()
