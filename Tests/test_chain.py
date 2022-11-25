import sys

sys.path.insert(0, "C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Code")

from classes.data_import import DataImport
from classes.data_cleaning import DataCleaning
from classes.data_analysis import DataAnalysis

importer = DataImport()
cleaner = DataCleaning()
analyzer = DataAnalysis()

importer.import_txt("Data\\Miebach\\ASOS\\10k_Test.txt")

cleaner.get_data(importer)
cleaner.remove_blanks()
cleaner.to_numeric()
cleaner.remove_duplicate_rows()
cleaner.head()

analyzer.get_data(cleaner)
analyzer.basic_anylsis()
analyzer.results_basic_analysis()