import pandas as pd

import sys

sys.path.insert(0, "C:\\Users\\Max\\Documents\\Uni\\Masterarbeit\\Code")

from classes.outlier import Outlier

def check_density_with_volume(data: pd.DataFrame, column_weight: str, column_volume: str, column_prim_key: str, max_den: float, min_den: float ,unit_ratio: float = 1, print_stats: bool = True) -> Outlier:

    """
    
    unit_ratio:
        Factor to ensure matching untis for weight and volume (kg or g vs. liter or mm3)
        Unit_ratio is multiplied with ratio from weight and volume. 
    """

    outlier = Outlier()
    num_outlier = 0

    for index, weight in enumerate(data[column_weight]):

        density = (weight / data[column_volume][index]) * unit_ratio

        if density <= max_den and density >= min_den:
            pass

        else:
            num_outlier += 1
            outlier.add_outlier(data[column_prim_key][index], density)

    if print_stats:
        print()

    return outlier


def check_density_with_xyz(data: pd.DataFrame, column_weight: str, column_x: str, column_y: str, column_z: str, column_prim_key: str, max_den: float, min_den: float ,unit_ratio: float = 1) -> dict:

    """
    
    unit_ratio:
        Factor to ensure matching untis for weight and volume (kg or g vs. liter or mm3)
        Unit_ratio is multiplied with ratio from weight and volume. 
    """

    outlier = []
    num_outlier = 0

    for index, weight in enumerate(data[column_weight]):

        density = (weight / (data[column_x][index] * data[column_y][index] * data[column_z][index])) * unit_ratio

        if density <= max_den and density >= min_den:
            pass

        else:
            num_outlier += 1
            outlier.append((data[column_prim_key][index], density))

    return {"Num": num_outlier, "Outlier": outlier}

