import sys

sys.path.insert(0, "C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Code")

import time
import pandas as pd

import settings


class SKU_Group:

    """
    A class used to store all information about a article in different sizes.
    Product data is stored in self.df as pd.DataFrame. 
    All analysis methods can be performed. 
    Store results of analysis with add_attr method as class attribute. 

    ...

    Attributes
    ----------
    id :
        id which connects all product in SKU-Group and is used as key in group dict 
    df :
        pandas DataFrame used to store articles and their attributes
    
    Methods
    ---------


    """

    def __init__(self, id: str, column_names: list) -> None:

        """
        __init__ creates attribute self.id and an empty DataFrame with column_names

        Parameters
        ----------
        id :
            id which identifies same articles
        column_names :
            list with all column_names
        
        """

        self.id = id
        self.df = pd.DataFrame(columns = column_names)

    def __repr__(self):

        """
        Object is represented by id and the number of articles (len(self.df))
        """

        return f" {self.id} [{len(self.df)} SKUs]"

    def head(self, n = settings.head_rows):

        """
        Same method as df.head()

        Parameters
        ----------
        n :
            number of rows that are displayed. Default is defined by settings.head_rows
        """
        # If n bigger than len(self.df), .head() raises an error
        if n > len(self.df):
            n = len(self.df)

        print(self.df.head(n))

    def add_df_row(self, row_data):

        """
        Method adds a new row to existing dataframe (self.df).
        Index will be reconverted to 0 - (n-1)

        Parameters
        ----------
        row_data :
            panda series from another DataFrame
        """

        self.df = pd.concat([self.df, row_data.to_frame().T], ignore_index = True)

    def add_attr(self, name, value):

        """
        Creates a new class variable and assigns value.
        Attribute can be accessed via self.name in class or class_name.name.

        Parameters
        ----------
        name :
            name of new attribute
        value:
            value that gets assigned to new attribute
        """

        setattr(self, name, value)

    def to_numeric(self, print_dtypes = False, *columns: str) -> None:

        """
        The method uses pd.to_numeric to transfrom dtype of columns to int or float depending on values in column.
        If no columns are given, all possible columns will be transformed.
        Use methods 'transfrom_numbers_int' or 'transform_numbers_float' to convert into specific dtype. XXX
        
        Parameters
        ----------
        print_dtypes :
            Wheater or not the new dtypes of transformed columns are printed. Default: False
        *columns (*args) :
            columns which shall be transformed to integer. 
        """

        if len(columns) == 0: 

            for column in self.df:

                try:
                    self.df[column] = pd.to_numeric(self.df[column])
                    if print_dtypes: print(f"{column} -> {type(self.df[column].dtypes)}")
                
                except:
                    pass

        else:
            
            for column in columns:

                self.df[column] = pd.to_numeric(self.df[column])
                if print_dtypes: print(f"{column} -> {type(self.df[column].dtypes)}")

    def astype(self):
        pass

    def transform_size_format(self, column):

        for index, size in enumerate(self.df[column]):

            if len(size) >= 3:

                x_num = size.count("X")
                new_size = str(x_num) + "X" + size[-1]

                self.df.loc[index, column] = new_size

    def check_str_sizes(self, column: str, sizes: list):
        
        # The number of articles is restricted to number of sizes.
        if len(self.df) > len(sizes):
            raise Exception(f"Group has more articles ({len(self.df)}) than different sizes ({len(sizes)}")

        found_list = [False for x in sizes]

        for index, size in enumerate(self.df[column]):

            i = sizes.index(size)
            print(index, size, i)

            found_list[i] = True
        
        print(sizes)
        print(found_list)

        f_t = 0
        t_f = 0

        for i in range(1, len(found_list)):

            if found_list[i-1] == False and found_list[i] == True:
                f_t += 1

            elif found_list[i-1] == True and found_list[i] == False:
                t_f += 1

        print(f"False to True{f_t} True to False: {t_f}")

        if f_t > 1 or t_f > 1:
            print(f"Warning regarding sizes")
            print(sizes)
            print(found_list)

        #XXX