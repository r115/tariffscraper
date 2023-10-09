from pdfquery import PDFQuery
from pathlib import Path
from os import path

class KcbTariffParser:
    year = 2023

    def __init__(self, year):
        self.year = year

    def load_file(self):
        current_path=path.dirname(path.abspath(__file__))

        print(current_path)
        print('File name:', path.dirname(path.abspath(__file__)))

        pdf = PDFQuery(current_path +'/tariffs/' + self.year + '.pdf')
        pdf.load()

        return pdf
    
    def parse(self):
        pdf = self.load_file()

        print(pdf.pq('LTPage[pageid=\'1\']').text())
        print("Parsing KCB")
        return self
    