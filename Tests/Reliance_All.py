import sys

sys.path.insert(0, "C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Code")

from importer_class import Data_Importer
import settings
import categories.utils
import categories.relevancy
import categories.completeness
import visualize

importer = Data_Importer()

importer.import_txt("Data\\Miebach\\Reliance\\Products_All.txt")

importer.remove_blanks()

importer.remove_1000_separator(["Weight", "Length", "Width", "Height"], ".")

importer.replace_char(["Weight", "Length", "Width", "Height"], ",", ".")

importer.to_numeric()

importer.unify_units(importer.data, "Weight UoM", "Weight", "G", settings.to_gramm)

print(categories.relevancy.check_relevancy(importer.data))
print(categories.completeness.create_column_dict(importer.data, "Unit of Dimension"))

importer.unify_units(importer.data, "Unit of Dimension", ["Weight", "Length", "Height"], "MM", settings.to_mm)

importer.head()

data_dict = categories.completeness.create_column_dict(importer.data, "Storage Condition")

visualize.visualize_distribution(data_dict)