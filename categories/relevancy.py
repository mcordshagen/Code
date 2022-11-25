import pandas as pd
from typing import Tuple

import settings

class Relevancy:

    def __init__(self):

        self.relevancy = None
        self.inferences = None

    def check_relevancy(self, data: pd.DataFrame):

        """
        Method checks how many different values are in each column. If there is only one value, the column has no relevancy.
        Method returns boolean value if there is at least one column with only one unique value and a dict with all columns and unique values in the column.   

        data : 
            Data to check as pandas dataframe
        """

        self.relevancy = {}

        # Count number of unique values in every column
        for column in data:

            unique_values = data[column].nunique()

            self.relevancy[column] = unique_values
        
        return self.relevancy

    def print_relevancy(self) -> None:

        print("RESULTS: Relevancy")
        print("Col: Column Name --> Number of Unique Values --> Relevant or not")

        if self.relevancy == None:
            print("Relevancy not anaylzed yet")

        else:

            for col in self.relevancy:
                print(f"Col: {col} --> {self.relevancy[col]} --> {True if self.relevancy[col] != 1 else False }")

        print()

    def infer_from_col1_to_col2(self, data: pd.DataFrame, from_col: str, to_col: str) -> bool:

        # Get a list of all different values from column 1
        list_from_col = list(data[from_col].unique())

        # Create a dict from the list with an empty list as value
        value_dict = {}
        for key in list_from_col:
            value_dict[key] = []

        # Iterate through columns 
        for index, value_from_col in enumerate(data[from_col]):

            value_to_col = data.loc[index, to_col]
            
            # Add value from column 2 to dict entry from column 1 if not already in list
            if value_to_col not in value_dict[value_from_col]:
                value_dict[value_from_col].append(value_to_col)

        for key in value_dict:

            if len(value_dict[key]) > 1:
                return False

        return True

    def inferences_all(self, data):

        col_list = list(data)

        n_calculations = len(data.columns) ** 2
        counter = 0

        from_list = []
        to_list = []

        for col in col_list:
            from_list.append("from_" + col)
            to_list.append("to_" + col)
        
        self.inferences = pd.DataFrame(columns = to_list, index = from_list)

        print(f"0/{n_calculations} inferences checked", end = " ")

        for col_1 in col_list:

            for col_2 in col_list:
                
                #print("1", col_1, "2", col_2)
                if col_1 == col_2:
                    self.inferences.loc["from_" + col_1, "to_" + col_2] = "X"
                    result = "X"

                else:
                    result = self.infer_from_col1_to_col2(data, col_1, col_2)
                    self.inferences.loc["from_" + col_1, "to_" + col_2] = result

                counter += 1

                if counter % 10 == 0 or counter == n_calculations:
                    print(f"\r{counter}/{n_calculations} inferences checked", end = " ")

        print()
        print()

    def print_inferences():

        print("RESULTS: Inferences")
        