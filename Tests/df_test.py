import numpy as np
import pandas as pd
import sys

sys.path.insert(0, "C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Code")

import categories.free_of_error
import categories.relevancy
import settings

columns = ["SKU", "Name", "Weight in kg", "Volume in l"]
data = [("100", "Sugar", 1, 1), ("101", "Milk", np.nan, 1.5), ("102", "Toiletpaper", 0.5, np.nan), ("104", "Butter1", np.nan, np.nan), ("104", "Butter1", 0.25, 0.1)]

df = pd.DataFrame(data, columns = columns)

row = pd.Series(("105", "Cheese", 12, 4), index = columns)

print(row, type(row))

new_df = df.append(row, ignore_index = True)

print(new_df)
print()

concat_df = pd.concat((df, row.to_frame().T), ignore_index = True)

print(concat_df)

dtype_list = []

for column in df:

    if pd.api.types.is_numeric_dtype(df[column]):
        dtype_list.append(column)

print(df.dtypes, type(df.dtypes), list(df.dtypes))
print(dtype_list)

from_columns = []
to_columns = []

for col in columns:

    from_columns.append("from_" + col)
    to_columns.append("to_" + col)

print(from_columns)
print(to_columns)

infer = pd.DataFrame(columns = to_columns, index = from_columns)

print(infer.head())

print(list(df))