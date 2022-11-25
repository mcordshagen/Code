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

importer.import_csv("Data\\Miebach\\X\\Short_Test_Mini.csv")

importer.remove_columns("Unnamed: 0")

importer.to_numeric()

importer.unify_two_columns("Nettogewicht.in.g", "NettoGew", "NettoGewicht")
importer.unify_two_columns("Bruttogewicht.in.g", "BruttoGew", "BruttoGewicht")

importer.remove_columns("Nettogewicht.in.g", "NettoGew", "Bruttogewicht.in.g", "BruttoGew")

importer.head(18)

importer.group_data("VKArtikel")

print(importer.groups)
print()

print(relevancy.check_for_bijection(importer.data, "FarbNr", "FarbText"))
print(relevancy.check_for_bijection(importer.data, "FarbText", "FarbNr"))