import sys

sys.path.insert(0, "C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Code")

from importer_class import Data_Importer

import settings
from archive.unsupervised import Unsupervised_Learning

import categories.completeness

importer = Data_Importer()

importer.import_txt("Data\\Miebach\\ASOS\\10k_Test.txt")

importer.remove_columns("SKU", "Hanging.Flag")

importer.transform_binary_feature("Gender", "WOMENS", "MENS")

category_dict = categories.completeness.create_column_dict(importer.data, "Category")
print(category_dict)
print()

for key in category_dict:
    category_dict[key] = {}

for index, value in enumerate(importer.data["Category"]):

    if importer.data["Size"][index] in category_dict[value]:
        category_dict[value][importer.data["Size"][index]] += 1
    else:
        category_dict[value][importer.data["Size"][index]] = 1

for sub_dict in category_dict:
    print(f"{sub_dict}: {category_dict[sub_dict]}")

"""
importer.transform_categorical("Package.Type")
importer.transform_categorical("Category")
"""

importer.head()
