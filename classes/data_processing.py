import sys

sys.path.insert(0, r"C:\Users\Max\Documents\Uni\Masterarbeit\Code")

import pandas as pd

import settings

class DataProcessing:

    def __init__(self):

        self.data = None
        self.raw_data = None 

    def head(self, n: int = settings.head_rows, data: str = "data") -> None:
        
        """
        Method uses pandas head-method to display first n rows.
        Can be used to show head from self.data or self.raw_data

        Parameters
        ----------
        n :
            Number of rows that shall be displayed. 
            Default is defined in settings.head_rows
        data : 
            'data' to display head of self.data or 'raw' to display head of self.raw_data

        """

        if n > len(self.data):
            n = len(self.data)

        if data == "data":
            print(self.data.head(n))

        elif data == "raw":
            print(self.raw_data.head(n))
        
        else:
             raise ValueError(f"data has to be 'data' or 'raw' but data is '{data}'")

        print()

    def get_data(self, obj) -> None:

        self.data = obj.data
