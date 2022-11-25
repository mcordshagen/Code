from data_processing import DataProcessing
from classes.sku_group import SKU_Group

class DataGroup(DataProcessing):

    def __init__(self):
        
        super().__init__()

    def group_data(self, *columns):

        """
        Method groups SKUs in different sizes in new pd.DataFrames.
        All new dfs are stores in a dict. The SKU is used as key.

        Parameters
        ----------
        columns (*args) :
            columns that can be used to identify the same product in different colors, sizes etc. 
        """

        self.groups = {}

        column_names = list(self.data.columns) # Create a list with all column names

        for index, value in enumerate(self.data[columns[0]]):
            
            # Create id that can be used to identify uniquely same products
            id = ""

            for column in columns:

                id += str(self.data[column][index])

                # Add '_' between two strings to improve readability if not last column
                if column != columns[-1]:
                    id += "_"

            # Check if id already in groups, if not create new entry
            if id not in self.groups:
                
                self.groups[id] = SKU_Group(id, column_names)
                self.groups[id].add_df_row(self.data.loc[index])

            # Add new product to exisiting group
            else:
                
                self.groups[id].add_df_row(self.data.loc[index])