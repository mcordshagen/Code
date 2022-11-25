import sys
from tabnanny import verbose

sys.path.insert(0, "C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Code")

from importer_class import Data_Importer

import settings
from archive.unsupervised import Unsupervised_Learning

import categories.completeness

from kmodes.kprototypes import KPrototypes

importer = Data_Importer()

importer.import_txt("Data\\Miebach\\Reliance\\Products_All.txt")

importer.remove_blanks()
importer.remove_1000_separator(".", "Weight", "Length", "Height", "Width")
importer.replace_char(",", ".", "Weight", "Length", "Height", "Width")
importer.to_numeric("Weight", "Length", "Height", "Width")

importer.unify_units("Weight UoM","G", settings.to_gramm, "Weight")
importer.unify_units("Unit of Dimension", "MM", settings.to_mm, "Length", "Width", "Height")

importer.remove_columns("Article", "Article description", "Weight UoM", "Unit of Dimension")
 
importer.head()

n = 4

kproto = KPrototypes(n_clusters = n)
kproto.fit(importer.data, categorical = [1]) 
clusters = list(kproto.predict(importer.data, categorical = [1]))
importer.data["Cluster"] = list(clusters)

cluster_sizes = {}
amount = 0

importer.head()

for i in range(1, n + 1):
    cluster_sizes[i] = clusters.count(i)
    amount += cluster_sizes[i]

print(amount, cluster_sizes)