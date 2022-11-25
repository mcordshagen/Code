import sys

sys.path.insert(0, "C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Code")

from importer_class import Data_Importer

import settings

import categories.relevancy as relevancy
import categories.redundancy as redundancy
import categories.completeness as completeness
import categories.free_of_error as free_of_error
import categories.math_stats as math_stats
import visualize


importer = Data_Importer()

importer.import_txt("Data\\Miebach\\ASOS\\10k_Test.txt")

importer.remove_blanks()

importer.to_numeric()

importer.head(50)

formats = free_of_error.format_analysis(importer.data, "Size")





print(f"Quantile: {importer.data['Unit.Weight'].quantile()}")