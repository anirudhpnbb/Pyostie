import csv


class CSVParser:
    
    def __init__(self, filename, delimiter):
        """

        Parameters
        ----------
        filename : The file that needs to be processed.
        delimiter : By default ','. Can be changed if any other delimiter is needed.

        """
        self.file = filename
        self.delimiter = delimiter

    def extract_csv(self):
        """

        Returns
        -------
        CSVParser for csv files.

        """
        with open(self.file) as file:
            output = csv.reader(file, delimiter=self.delimiter)
            return ' '.join([' '.join(row) for row in output])
