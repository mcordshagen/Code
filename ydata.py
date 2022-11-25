from ydata_quality import DataQuality
import pandas as pd
import sys

sys.path.insert(0, "C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Code")

from importer_class import Data_Importer
import categories.completeness as completeness

importer = Data_Importer()

#importer.import_txt("Data\\Miebach\\ASOS\\10k_Test.txt")

#importer.to_numeric()

#census_10k = pd.read_csv("Data\\ydata\\census_10k.csv")
asos_100 = pd.read_csv("Data\\Miebach\\ASOS\\100_Test.csv")

print(asos_100.head())

dq = DataQuality(df = asos_100)

print(completeness.create_column_dict(asos_100, "Unit.Weight"))
print(completeness.create_column_dict(asos_100, "Package.Type"))
print(completeness.create_column_dict(asos_100, "Hanging.Flag"))
print(completeness.create_column_dict(asos_100, "Size"))
print(completeness.create_column_dict(asos_100, "Category"))
print(completeness.create_column_dict(asos_100, "Gender"))
print()

results = dq.evaluate()

print("Done")