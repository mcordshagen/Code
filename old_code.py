def transform_categorical(self, *columns: str) -> None:

        """
        Method transforms a categorical feature into integer values. 
        XXX eigentlich nicht machbar 
        
        """

        for column in columns:
        
            replacement = 0

            replacement_dict = {}

            for index, value in enumerate(self.data[column]):

                if value in replacement_dict:
                    self.data.loc[index, column] = replacement_dict[value]

                else:
                    self.data.loc[index, column] = replacement
                    replacement_dict[value] = replacement
                    replacement += 1

            print(f"replacement_dict: {replacement_dict}")

def transform_binary_feature(self, column: str, val_0: str, val_1: str) -> None:

        """
        Method transform a non-integer binary feature (e.g., True or False, Yes or No) into 0 and 1.

        Parameters
        ----------
        column :
            column with binary feature
        val_0 :
            value that shall be transformed into 0
        val_1 :
            value that shall be transformed into 1
        """

        for index, value in enumerate(self.data[column]):

            if value == val_0:
                self.data[column][index] = 0
            
            elif value == val_1:
                self.data[column][index] = 1

            else:
                raise ValueError(f"{value} at index {index} is not {val_0} or {val_1}.")