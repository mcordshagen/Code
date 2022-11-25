import settings
import pandas as pd

class Redundancy:

    def __init__(self):
        pass

    def check_for_redundancies(data):

        """
        Method checks if all rows are unique. Method returns True if so and False otherwise.

        data : data to check as pandas dataframe
        """

        key_string_list = []

        for i in range(len(data)):

            key_string = ""
        
            for value in data.loc[i]:
                key_string += str(value)

            key_string_list.append(key_string)

            if (i + 1) % settings.uniqueness_tracker == 0 or (i + 1) == len(data):
                print(f"\r{i + 1} / {len(data)} key_strings", end = "")

        print()

        if len(set(key_string_list)) == len(key_string_list):
            return True
        else:
            return False

    def check_for_duplicates_in_column(data: pd.DataFrame, column: str) -> bool:
        
        if data.shape[0] == data[column].nunique():
            return True
        else:
            return False
