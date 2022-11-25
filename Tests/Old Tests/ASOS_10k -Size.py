import sys

sys.path.insert(0, "C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Code")

from importer_class import Data_Importer

import settings
from kmodes.kprototypes import KPrototypes

import categories.completeness

importer = Data_Importer()

importer.import_txt("Data\\Miebach\\ASOS\\10k_Test.txt")

importer.transform_binary_feature("Gender", "WOMENS", "MENS")

importer.remove_columns("Hanging.Flag", "Size", "SKU")

importer.remove_duplicate_rows()

importer.transform_categorical("Category", "Package.Type")

importer.head()

n_clusters = 4
categoricals = [1, 2]
kproto = KPrototypes(n_clusters = n_clusters)
kproto.fit(importer.data, categorical = categoricals) 
clusters = list(kproto.predict(importer.data, categorical = categoricals))
importer.data["Cluster"] = list(clusters)

cluster_sizes = {}
total = 0

importer.head()

for i in range(1, n_clusters + 1):
    cluster_sizes[i] = clusters.count(i)
    total += cluster_sizes[i]

print(total, cluster_sizes)

