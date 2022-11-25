import sys

sys.path.insert(0, "C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Code")

from importer_class import Data_Importer

import settings


importer = Data_Importer()

importer.import_csv("Data\\Miebach\\X\\Short_Test_Sizes.csv")

importer.remove_columns("Unnamed: 0")

importer.to_numeric()

importer.head(importer.data_len)

importer.group_data("VKArtikel")

print(importer.groups)

importer.groups["71017565101101"].transform_size_format("Groesse")

importer.groups["71017565101101"].head()

#importer.groups["71017565201800"].check_str_sizes("Groesse", ["4XS", "3XS", "2XS", "XS", "S", "M", "L", "XL", "2XL", "3XL", "4XL"])

