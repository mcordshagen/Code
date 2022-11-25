import pandas as pd
import numpy as np
from typing import Union

import settings

class FreeOfError:

    def __init__(self):
        
        self.formats = None
        self.lenghts = None

    def check_length_of_values(self, data: pd.DataFrame, column: str, correct_length: Union[int, list]) -> dict:

        """
        Method checks the length of value in given column. Values with false length are counted and added to a list.
        Please note that len() works only for strings. So numbers will be transformed to strings. 
        Therefore "." counts as char and will be counted as well. 
        Method returns dict with column, number of values with wrong length and list of all these values.

        data : pd.DataFrame with data
        column : column to check lenght
        correct_length : int or list with value(s) of correct length
        """

        num_wrong_length = 0
        value_list = []
        
        if type(correct_length) == int:
            correct_length = [correct_length]

        for value in data[column]:

            if len(str(value)) not in correct_length:

                num_wrong_length += 1 
                value_list.append(value) #XXX convert to outlier list 

        return {"Column": column, "Num": num_wrong_length, "List": value_list}

    def check_lengths(self, data):

        self.lenghts = {}

        for col in data:

            col_lengths = {}

            for value in data[col]:

                l = len(str(value))

                if l in col_lengths:
                    col_lengths[l] += 1

                else:
                    col_lengths[l] = 1

            self.lenghts[col] = dict(sorted(col_lengths.items(), key=lambda item: item[1], reverse = True))

    
    def print_lengths(self) -> None:

        print("RESULTS: Lengths")
        print("Col: Column Name {Length: Frequency}")

        for col in self.lenghts:
            print(f"Col: {col} {self.lenghts[col]}")

        print()

    def check_range(self, data: pd.DataFrame, column: str, max_val: float, min_val: float) -> dict:

        """"
        Method checks for every value in column, if it is bigger than maximum value or smaller than minimum value. 
        This works only for columns with numeric values. Max_val and min_val are both mandatory arguments.
        If the comparison should only be done with maximum or minimum value, enter unrealistic values. 
        Method returns a dict with given column, number of outliers and a list with tuples including index and outlier value. 

        Parameters
        ----------
        data:
            pd.DataFrame with data

        column:
            column with numeric values to calculate average

        max_val:
            maximum value that shall not be exceeded 
        
        min_val:
            minimum value that shall not be fallen short of
        """

        num = 0
        outlier_list = []

        for index, value in enumerate(data[column]):

            if value <= max_val and value >= min_val:
                pass
            else:
                num += 1
                outlier_list.append((index, value))

        return {"Column": column, "Num": num, "List": outlier_list}

    def valid_chars(self, data, columns: Union[str, list], char_list: Union[str, list], allow_cap = True) -> bool:

        if char_list == "numbers":
            allowed_chars = "0123456789"
        
        elif char_list == "abc":
            allowed_chars = "abcdefghijklmnopqrstuvwxyz"

        if allow_cap:
            allowed_chars += allowed_chars + allowed_chars.upper()

        if type(columns) == str:
            column_list = [columns]

        else:
            column_list = columns

        print(column_list)

        outlier_list = []
        all_ok = True

        for column in column_list:

            for index, string in enumerate(data[column]):

                if not all(char in allowed_chars for char in string):
                    outlier_list.append((string, index))
                    all_ok = False

        return all_ok, outlier_list


    def format_analysis(self, data: pd.DataFrame, special_chars: list = []):

        abc = "abcdefghijklmnopqrstuvwxyz"
        abc_cap = abc.upper()
        numbers = "0123456789"

        self.formats = {}

        for col in data:

            format_dict = {}

            for value in data[col]:

                string = str(value)
                format = ""

                for char in string:

                    if char in abc:
                        format += "l" # Lowercase Letter

                    elif char in abc_cap:
                        format += "L" # Uppercase Letter

                    elif char in numbers: 
                        format += "D" # Digit

                    else:
                        format += char

                if format in format_dict:
                    format_dict[format] += 1
                else:
                    format_dict[format] = 1

            self.formats[col] = format_dict
        #return (column, {key: value for key, value in sorted(format_dict.items(), key=lambda item: item[1], reverse = True)})

    def print_formats(self):

        print("RESULTS: Formats")
        print("D - Digit, L - Uppercase Letter, l - Lowercase Letter")

        if self.formats == None:
            print("Formats not analyzed yet")
        
        else:
            for col in self.formats:
                print(f"Col: {col} {self.formats[col]}")
        
        print()

