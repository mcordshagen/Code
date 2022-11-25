import sys

sys.path.insert(0, "C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Code")

from importer_class import Data_Importer

import settings

import categories.relevancy
import categories.redundancy
import categories.completeness
import categories.free_of_error
import categories.math_stats
import categories.utils


importer = Data_Importer()

importer.import_txt("Data\\Miebach\\ASOS\\Master.txt")

importer.remove_blanks()

importer.to_numeric()

importer.head()

sizes = categories.completeness.create_column_dict(importer.data, "Size")

print(len(sizes), type(sizes), sizes)

categories.utils.save_dict_csv(sizes, "C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Code\\Data\\Miebach\\ASOS\\Sizes_ASOS.csv")