import sys

sys.path.insert(0, "C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Code")

import pandas as pd

import relevancy

def basic_analysis(data: pd.DataFrame):

    

    irrelevant_columns = relevancy.check_relevancy(data)

    if len(irrelevant_columns) > 0:
        print(f"Irrelevant columns: {irrelevant_columns}")
    else:
        print("There is no irrelevant column")

    