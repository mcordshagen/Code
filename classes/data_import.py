import sys

sys.path.insert(0, "C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Code")

import time
import numpy as np
import pandas as pd

from classes.data_processing import DataProcessing
import categories.utils as utils

class DataImport(DataProcessing):

    def __init__(self):

        super().__init__()

    def import_txt(self, path: str, dtype: np.dtype = str, delimiter: str = "\t"):

        """
        Import data from txt-file. Data is stored in self.data as well as in self.raw_data.

        Parameters
        ----------
        path : 
            path to txt-file 
        dtype :
            data type
        delimiter : 
            delimiter is used to separate values, by deafult it is tab stop
        """

        start_time = time.time()

        inbound_np = np.loadtxt(path, dtype = str, delimiter = "\t") # Import txt with numpy
        index_row = [inbound_np[0]] # Copy column names out of first row
        columns_list = [] # Create list with column names to use it as index for dataframe
        for column_names in index_row[0]: 
            columns_list.append(column_names.strip())
        inbound_np = np.delete(inbound_np, (0), axis = 0) # Delete first column with name from array

        self.data = pd.DataFrame(inbound_np, columns = columns_list) # Convert array into pandas dataframe and save dataset

        self.data_len = len(self.data)

        self.raw_data = self.data

        exe_min, exe_s = utils.calc_processing_time(start_time)

        print(f"Data imported from: {path} Duration: {exe_min} min {exe_s} s")
        print()

    def import_csv(self, path):

        """
        Import data from csv-file. Data is stored in self.data as well as in self.raw_data.

        Parameters
        ----------
        path : 
            path to csv-file 
        """

        start_time = time.time()
        
        self.data = pd.read_csv(path, delimiter = ",")
        self.raw_data = self.data

        exe_min, exe_s = utils.calc_processing_time(start_time)

        print(f"Data imported from: {path} Duration: {exe_min} min {exe_s} s")
        print()

    def import_xlsx(self, path: str, sheet_name: str) -> None:

        """
        Import data from xlsx-file. Data is stored in self.data as well as in self.raw_data.

        Parameters
        ----------
        path : 
            path to csv-file 
        
        sheet_name :
            name of sheet eith data
        """
        
        start_time = time.time()

        self.data = pd.read_excel(path, sheet_name = sheet_name)
        self.raw_data = self.data

        exe_min, exe_s = utils.calc_processing_time(start_time)

        print(f"Data imported from: {path} Duration: {exe_min} min {exe_s} s")
        print()

        