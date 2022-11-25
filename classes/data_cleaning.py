import sys

sys.path.insert(0, "C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Code")

import time
import numpy as np
import pandas as pd
from typing import List, Dict

from classes.data_processing import DataProcessing
import settings
import categories.utils as utils

class DataCleaning(DataProcessing):

    def __init__(self):

        super().__init__()


    def transform_dtype(self, dtype: str, *columns, print_dtypes = False) -> None:

        """
        The method uses pandas astype method to transform columns into desired dtype.
        If no columns are given, all possible columns will be transformed.
        Use methods 'transfrom_numbers_int' or 'transform_numbers_float' to convert into specific dtype. 
        
        Parameters
        ----------
        dtype :
            Select desired dtype.
            dtype can be a Python dtype or numpy.dtype
        *columns (*args) :
            columns which shall be transformed to a numeric dtype. 
        print_dtypes :
            Wheater or not the new dtypes of transformed columns are printed. Default: False
        """

        if len(columns) == 0: 

            conversion_dict = {}

            for column in self.data:

                try:
                    self.data[column] = self.data[column].astype(dtype)
                    if print_dtypes: conversion_dict[column] = self.data[column].dtypes
                
                except:
                    pass

            print(f"Conversions: {conversion_dict}")

        else:
            
            for column in columns:

                self.data[column] = self.data[column].astype(dtype)


    def to_numeric(self, print_dtypes = False, *columns: str) -> None:

        """
        The method uses pd.to_numeric to transfrom dtype of columns to int or float depending on values in column.
        If no columns are given, all possible columns will be transformed.
        Use methods 'transfrom_numbers_int' or 'transform_numbers_float' to convert into specific dtype. 
        
        Parameters
        ----------
        print_dtypes :
            Wheater or not the new dtypes of transformed columns are printed. Default: False
        *columns (*args) :
            columns which shall be transformed to a numeric dtype. 
        """

        if len(columns) == 0: 

            for column in self.data:

                try:
                    self.data[column] = pd.to_numeric(self.data[column])
                    if print_dtypes: print(f"{column} -> {type(self.data[column].dtypes)}")
                
                except:
                    pass

        else:
            
            for column in columns:

                self.data[column] = pd.to_numeric(self.data[column])
                if print_dtypes: print(f"{column} -> {type(self.data[column].dtypes)}")


    def replace_char(self, old_char: str, new_char: str, *columns) -> None:

        """
        Method replaces a specific char in a string with another char.
        If new_char is set to an empty string (""), the old char is only removed and not replaced.
        Can be also used to replace German Umlaute (ä,ö,ü) or other lanuguage-specific chars.
        
        Parameters
        ----------
        old_char : 
            char to replace
        new_char :
            char which replaces the old_char
        *columns (*args) :
            columns where old_char shall be replaced
        """

        for column in columns:

            for index, string in enumerate(self.data[column]):

                if old_char in string:

                    self.data[column][index] = self.data[column][index].replace(old_char, new_char)


    def remove_1000_separator(self, separator: str, *columns: str):

        """
        Method removes thousands separator from strings.
        If numbers which are saved as string contain thousands separator a conversion into another data type is not possible.
        
        Parameters
        ----------
        separator : 
            char which is used as separator
        *columns (*args) :
            columns with separator
        """

        for column in columns:

            for index, string in enumerate(self.data[column]):

                if separator in string:

                    self.data.loc[index, column] = self.data[column][index].replace(separator, "")


    def remove_blanks(self, *columns) -> None:

        """
        Method removes blanks in front and at the end of strings with strip-method.
        Specific can be provided. If no columns are provided first value of every column is check, if surplus blanks exist.
        After checking all columns, columns with surplus blanks are stripped. 
        Stripping large datasets can be time-consuming. Therefore execution time is measured as well as current progress is displayed in console.   
        
        Parameters
        ----------
        *columns (*args) :
            columns that shall be stripped
        """

        start_time = time.time()

        if len(columns) == 0:
            column_list = []

            for column in self.data:
                
                start_len = len(self.data[column][0])

                new_len = len(self.data[column][0].strip())

                if new_len != start_len:
                    column_list.append(column)

            if len(column_list) == 0:
                print("No blanks detected")
            else:
                print(f"Columns with blanks: {column_list}")

        else:
            column_list = columns

        data_entries = len(self.data) * len(column_list)
        overall_index = 0

        for column in column_list:

            for index, value in enumerate(self.data[column]):

                overall_index += 1

                self.data.loc[index, column] = self.data.loc[index, column].strip()

                if (overall_index + 1) % settings.remove_blanks_tracker == 0 or (overall_index + 1) == data_entries:
                    print(f"\r{overall_index + 1} / {data_entries} Blanks", end = "")

        exe_min, exe_s = utils.calc_processing_time(start_time)

        if len(column_list) != 0: print(f" removed in {exe_min} min {exe_s} s")


    def unify_units(self, unit_column: str , main_unit: str, unit_dict: dict, *value_columns) -> None:

        """
        Method converts value with different units into one unit (main_unit). 
        Therefore, unit_dicts are used which provide the correct conversion factors.
        Multilpe columns with the same unit conversion can be converted at the same time (e.g., length, width & height)
        settings file contains following unit_dicts:
            weight: to_gramm, to_kg, to_ton
            dimensions: to_mm, to_cm, to_dm, to_m 
        
        Parameters
        ----------
        unit_column :
            column with unit
        main_unit :
            unit which all values are transformed to
        unit_dict :
            dict with conversion factors.
            unit dicts can be found in settings file
        *value_columns (*args) :
            columns with values that shall be transformed into main unit

        """

        for index, unit in enumerate(self.data[unit_column]): # Iterate through values in columns

            if unit != main_unit: # Check if unit transformation is necessary
                
                for column in value_columns:

                    self.data.loc[index, column] = self.data[column][index] * unit_dict[unit]

                self.data.loc[index, unit_column] = main_unit

    
    def remove_duplicate_rows(self, ignore_index = True):

        """
        Method removes duplicte rows from DataFrame using pandas drop_duplicates method.

        Parameters
        ----------
        ignore_index :
            resulting DataFrame will have a consistent index from 0 to n - 1
        """

        old_len = len(self.data)
        self.data = self.data.drop_duplicates(ignore_index = ignore_index)

        duplicates = old_len - len(self.data)

        if duplicates == 0:
            print("No duplicates found")

        else:
            print(f"{duplicates} duplicate rows removed. New len: {len(self.data)}")


    def unify_two_columns(self, pri_col: str, sec_col: str, new_name: str, blacklist: list = [], add_standard_defects = True) -> int:

        """
        Unifys two columns with similar content. If primary column (pri_col) contains a valid value, this value is used. 
        Otherwise secondary column (sec_col) is checked for valid value. Value is also checked for np.nan which is not valid.
        If no column contains a valid value, np.nan is used. 
        After unifiying, np.nan are counted, printed and returned. 

        Parameters
        ----------
        pri_col :
            primary column
        sec_col :
            secondary column
        new_name :
            name of new column with unified values
        blacklist :
            list of invalid values
        add_standard_defects :
            option to extend blacklist with list of standard defects from settings
        """

        self.data[new_name] = ""

        if add_standard_defects:
            blacklist.extend(settings.standard_defects)

        for index, pri_val in enumerate(self.data[pri_col]):

            sec_val = self.data[sec_col][index]

            if pri_val not in blacklist or np.isnan(pri_val):

                self.data.loc[index, new_name] = pri_val

            elif sec_val not in blacklist or np.isnan(sec_val):
                
                self.data.loc[index, new_name] = sec_val

            else:

                self.data.loc[index, new_name] = np.nan

        number_nan = self.data[new_name].isna().sum()

        if number_nan != 0:
            print(f"For {number_nan} rows there is no valid value.")

        return number_nan

    def remove_n_chars(self, column: str, new_column: str, n: int, where: str = "end") -> None:

        """
        Method removes a specific number of chars for all values in a column and save new values in a new column.
        Be aware that all values in new column are strings. Dtype can be changed with to_numeric, if needed.
        
        Parameters
        ----------
        column :
            column to remove chars from
        new_column :
            new column that is created
        n :
            number of char that is removed
        where :
            chars can be removed from 'front' or 'end' of string. Default is 'end'
        """

        self.data[new_column] = ""

        for index, value in enumerate(self.data[column]):

            if where == "end":

                self.data.loc[index, new_column] = str(value)[:-3]

            elif where == "front":

                self.data.loc[index, new_column] = str(value)[-3:]

            else:
                raise Exception(f"where argument can only be 'front' or 'end' but it is '{where}'")


    def remove_columns(self, *columns: str) -> None:

        """
        Method removes columns from DataFrame with drop method from pandas.

        Parameters
        ----------
        columns (*args) :
            columns that shall be removed
        """

        for column in columns:
            self.data = self.data.drop(column, axis = 1)


    def rename_column(self, old_name: str, new_name: str) -> None:

        """
        Rename a column

        Parameters
        ----------
        old_name :
            name of column that shall be renamed
        new_name :
            new name of column
        """

        self.data = self.data.rename(columns = {old_name: new_name})

    def reset_index(self) -> None:

        """
        Resets the index from DataFrame to 0, 1, ... , n - 1
        """

        self.data.reset_index(drop = True)

    def drop_columns_with_value(self, value_dict: Dict[str, List[str]]) -> None:

        """
        Method removes rows from DataFrame if certain values appear in a column.
        After removing rows, uses reset_index reset index

        Parameters
        ----------
        value_dict :
            dict with a entry for every column (key = column) and a list of values        
        """

        key_list = list(value_dict.keys())
        removed_rows = 0

        for i in range(0, len(self.data)):

            for column in key_list:

                if self.data.loc[i, column] in value_dict[column]: # check if value in list of values to remove
                    self.data = self.data.drop(i, axis = 0)
                    removed_rows += 1

        self.data_len = len(self.data) 
        self.reset_index()
        print(f"{removed_rows + self.data_len} rows -> [{self.data_len} remain, {removed_rows} removed]")