import sys

sys.path.insert(0, "C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Code")

import pandas as pd
import csv
import time


def unify_units(data: pd.DataFrame, unit_column: str, value_column: str, main_unit: str, unit_dict: dict) -> None:

    for index, unit in enumerate(data[unit_column]): # Iterate through values in columns

        if unit in unit_dict: # Check if unit transformation is necessary
            
            # Perform transformation
            data.loc[index, value_column] = data[value_column][index] * unit_dict[unit]
            data.loc[index, unit_column] = main_unit

    return data

def save_dict_csv(data_dict: dict, path: str) -> None:

    with open(path, "w", newline = "") as f:
        w = csv.writer(f)
        w.writerows(data_dict.items())

    print(f"File successfully saved at {path}")

def generate_size_list(xs: int, xl: int, standard_sizes = ["S", "M", "L"]) -> list:

    """
    Method generates with a list of article sizes.
    List startes with small sizes and always contains standardsizes.

    Parameters
    ----------
    xs :
        highest number of xs (e.g., 2XS, 3XS)
        if 'xs' = 0 list starts with 's' as smallest size
    xl :
        highest number of xl (e.g., 2XL, 3XL)
        if 'xl' = 0 list ends with 'l' as biggest size
    standard_sizes :
        sizes that list always contains
    """

    size_list = []

    while xs > 1:

        size_list.append(f"{str(xs)}XS")
        xs -= 1

    if xs == 1:
        size_list.append("XS")

    size_list.extend(standard_sizes)

    if xl >= 1:

        size_list.append("XL")

        for i in range(2, xl + 1):
            size_list.append(f"{str(i)}XL")
            
    return size_list

def calc_processing_time(start_time: float) -> tuple:

    """
    Calculate execution time. 
    Returns tuple with minutes and seconds

    start_time :
        time the process has started
    """

    exe_time = time.time() - start_time
    exe_min = int(exe_time / 60)
    exe_s = int(exe_time - 60 * exe_min)

    return exe_min, exe_s