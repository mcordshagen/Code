import pandas as pd

class MathStats:

    def __init__(self):

        self.math_stats = None
        
        self.max_values = {}
        self.min_values = {}
        self.avg_values = {}
        self.median_values = {}
        self.std_values = {}

    def calc_all_values(self, data: pd.DataFrame, columns: list) -> None:

        self.math_stats = {}

        for col in columns:

            col_stats = {}
            
            col_stats["max"] = self.find_max(data, col)
            col_stats["min"] = self.find_min(data, col)
            col_stats["avg"] = self.calc_avg(data, col)
            col_stats["median"] = self.calc_median(data, col)
            col_stats["std"] = self.calc_std(data, col)

            self.math_stats[col] = col_stats
    
    
    def print_math_stats(self, decimals = 3):

        print("RESULTS: MathStats")

        for col in self.math_stats:

            print(f"Col: {col}", end = " ")

            for val in self.math_stats[col]:

                print(f"{val}: {round(self.math_stats[col][val], decimals)}", end = " ")

            print()

        print()

    def calc_avg(self, data: pd.DataFrame, column: str) -> float:

        """
        Method returns average of given column in pd.DataFrame.

        Parameters
        ----------
        data:
            pd.DataFrame with data

        column:
            column with numeric values to calculate average
        """

        return data[column].mean()

    def calc_median(self, data: pd.DataFrame, column: str) -> float:

        """
        Method returns median of given column in pd.DataFrame.

        Parameters
        ----------
        data:
            pd.DataFrame with data

        column:
            column with numeric values to calculate median
        """

        return data[column].median()

    def find_max(self, data: pd.DataFrame, column: str, arg = False) -> tuple:

        """
        Method returns maximum value and correpsonding index from given column in pd.DataFrame as tuple (max_value, max_index)

        Parameters
        ----------
        data:
            pd.DataFrame with data

        column:
            column with numeric values to find maximum
        
        arg :
            if True, method returns index of max value
        """
        
        if not arg:
            return data[column].max()

        else:
            return data[column].idxmax()

    def find_min(self, data: pd.DataFrame, column: str, arg = False) -> tuple:

        """
        Method returns minimum value and correpsonding index from given column in pd.DataFrame as tuple (min_value, min_index)

        Parameters
        ----------
        data:
            pd.DataFrame with data

        column:
            column with numeric values to find minmum

        arg :
            if True, method returns index of max value
        """

        if not arg:
            return data[column].min()

        else:
            return data[column].idxmin()

    def calc_std(self, data: pd.DataFrame, column: str) -> float:

        """
        Method returns standard deviation of given column in pd.DataFrame.

        Parameters
        ----------
        data:
            pd.DataFrame with data

        column:
            column with numeric values to calculate standard deviation
        """

        return data[column].std()

    def outside_n_sigma(self, data: pd.DataFrame, column: str, n: float) -> dict:

        sigma = self.calc_std(data, column)
        avg = self.calc_avg(data, column)

        plus_avg = avg + n * sigma
        minus_avg = avg - n * sigma

        outlier_list = []
        num = 0

        for index, value in enumerate(data[column]):

            if (value <= plus_avg) and (value >= minus_avg):
                pass
            
            else:
                outlier_list.append((index, value))
                num += 1

        return {"Column": column, "Num": num, "Avg": avg, "Std": sigma, "Outlier": outlier_list}
