import sys

sys.path.insert(0, "C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Code")

"""
- create_column_dict
- create_column_dict_type
- check_population_completeness
- check_column_completeness
- check_schema_completeness
"""

import settings
import pandas as pd
import categories.math_stats as math_stats
import math

class Completeness:

    def __init__(self):
        
        self.column_dicts = None


    def create_column_dict(self, data: pd.DataFrame, column: str) -> dict:

        """
        Method creates and returns a dictionary with all values as keys and their occurence frequency. 

        Parameters
        ----------
        data :
            DataFrame with data
        column :
            column which shall be investigated
        """

        column_dict = {}

        # Iterating over all values in column
        for value in data[column]:

            if value in column_dict: # If already in dict, increase counter by 1
                column_dict[value] += 1

            else: # Create new entry, if not already in dict
                column_dict[value] = 1

        return column_dict

    def create_column_dicts(self, data) -> dict:

        self.column_dicts = {}

        for column in data:

            self.column_dicts[column] = self.create_column_dict(data, column)

    def print_column_dicts(self):

        print("RESUTLS: Completeness")

        for col in self.column_dicts:

            print(f"Col: {col} {self.column_dicts[col]}")


    def create_column_type_dict(self, data: pd.DataFrame, column: str) -> dict:

        """
        Method creates and returns a dictionary with all dtypes in a column their occurence frequency.
        First entry of dict is the column name. 
        High quality data should have only one dtype. 

        Parameters
        ----------
        data :
            DataFrame with data
        column :
            column which shall be investigated
        """

        col_dict = {"column" : column}

        for value in data[column]:

            if type(value) in col_dict:
                col_dict[type(value)] += 1

            else:
                col_dict[type(value)] = 0

        return col_dict

    def check_population_completness(self, data: pd.DataFrame, column: str, population: list) -> dict:

        """
        This method checks if all expected values are in given column and how often they appear.
        For example it could be checked wheater all sizes (XS, S, M, L, XL, etc.) of a t-shirt are in the data-
        Method returns two dicts, one dict with all expected values and their frequency as well as a dict with not expected values and their frequency.  

        Parameters
        ----------
        data :
            DataFrame with data
        column :
            column which shall be investigated
        population :
            list with expected values
        """

        pop_dict = {}
        non_pop_dict = {}

        for i in population:
            pop_dict[i] = 0

        for value in data[column]:

            if value in pop_dict:
                pop_dict[value] += 1

            elif value in non_pop_dict:
                non_pop_dict[value] += 1

            else:
                non_pop_dict[value] = 1

        return {"Population Values": pop_dict, "Non Ppopulation Values": non_pop_dict}

    def check_column_completeness(self, data: pd.DataFrame, column: str, defects: list = [], use_standard_defects: bool = True, replace = "avg") -> int:

        """
        Method checks if data defects are in a column. Data defects are values like empty strings, NaN or similar. A list of typical defect values is provided in settings.data_defects.
        Please think about if 0 is a valid value or not. It is not incorporated in settings.data_defects. 
        
        Parameters
        ----------
        data : 
            Pandas Dataframe with data
        column : 
            Name of column to check
        defects : 
            List of values that are defects
        use_standard_defects : 
            Include standard defects defined in settings or not
        """

        if use_standard_defects:
            defects.extend(settings.standard_defects)

        defects = list(set(defects)) # Transform to set to remove duplicates and transform back to list
        
        defects_found = 0

        if replace == "avg":
            replace = math_stats.calc_avg(data, column)
        elif replace == "med":
            replace = math_stats.calc_median(data, column)

        for index, value in enumerate(data[column]):

            try:
                if value in defects or math.isnan(value):
                    defects_found += 1

                    if replace != None:
                        data[column][index] = replace

            except:
                if value in defects:
                    defects_found += 1

                    if replace != None:
                        data[column][index] = replace

        return data, defects_found


    def check_schema_completeness():
        pass