import xlrd


class XLSXParser:

    def __init__(self, filename):
        """

        :param filename:
        """
        self.file = filename

    def extract_xlsx(self):
        """

        :return:
        """
        out_list = []
        book = xlrd.open_workbook(self.file)
        for val in range(len(book.sheet_names())):
            sheet = book.sheet_by_index(val)
            for res in range(sheet.nrows):
                output = " " + " ".join(str(val_) for val_ in (sheet.row_values(res)))
                out_list.append(output)
        return out_list
