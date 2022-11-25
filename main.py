import pandas as pd
import numpy as np
import timeit
import time
import importer_class

# Script starts 
start = timeit.timeit()
start_time = time.time()



"""
# Import of txt-file and conversion to pd dataframe
inbound_np = np.loadtxt("C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Testdaten\\Miebach\\ASOS\\Inbound.txt", dtype = str, delimiter = "\t")
index_row = [inbound_np[0]] # Copy column names out of first row
columns_list = [] # Create list with column names to use it as index for dataframe
for column_names in index_row[0]: 
    columns_list.append(column_names)
inbound_np = np.delete(inbound_np, (0), axis = 0) # Delete first column with name from array
inbound = pd.DataFrame(inbound_np, columns = columns_list) # Convert array into pandas dataframe
"""
inbound = importer_class.import_txt("C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Testdaten\\Miebach\\ASOS\\Inbound.txt")
inventory_1 = importer_class.import_txt("C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Testdaten\\Miebach\\ASOS\\Inventory1.txt")
inventory_2 = importer_class.import_txt("C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Testdaten\\Miebach\\ASOS\\Inventory2.txt")
master =  importer_class.import_txt("C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Testdaten\\Miebach\\ASOS\\Master.txt")
outbound = importer_class.import_txt("C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Testdaten\\Miebach\\ASOS\\Outbound.txt")


print(inbound)
print(inventory_1)
print(inventory_2)
print(master)
print(outbound)

# Import done 
end = timeit.timeit()
print("Time for Import 1:", end - start)
print("Time for Import 2:", time.time() - start_time)
print()