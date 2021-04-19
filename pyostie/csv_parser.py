import csv


class CSVParser:

    def __init__(self, filename, delimiter=','):
        """

        :param filename:
        """
        self.file = filename
        self.delimiter = delimiter

    def extract_csv(self):
        """

        :return:
        """
        with open(self.file) as file:
            output = csv.reader(file, delimiter=self.delimiter)
            return ' '.join([' '.join(row) for row in output])
