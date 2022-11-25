from logging.handlers import DatagramHandler
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import categories.math_stats

def visualize_numeric_value(data: pd.DataFrame, column: str, sorted = True, digits = 3) -> plt:

    max_val = categories.math_stats.find_max(data, column)
    min_val = categories.math_stats.find_min(data, column)
    avg_val = categories.math_stats.calc_avg(data, column)
    med_val = categories.math_stats.calc_median(data, column)

    # Data
    x_axis = [i for i in range(len(data))]
    
    if sorted:
        y_axis = data[column].sort_values(ascending = False)
    else:
        y_axis = data[column]


    plt.plot(x_axis, y_axis)

    plt.xlim(1, len(data) + 1)
    plt.ylim(min_val[0] * 0.95, max_val[0] * 1.05)
    plt.ylabel(column)

    avg_label = "Average: " + str(round(avg_val, digits))
    med_label = "Median: " + str(round(med_val, digits))
    max_label = "Max: " + str(round(max_val[0], digits))
    min_label = "Min: " + str(round(min_val[0], digits))

    plt.axhline(y = avg_val, color = "red", label = avg_label) # Avg
    plt.axhline(y = med_val, color = "green", label = med_label) # Med
    plt.axhline(y = max_val[0], color = "yellow", label = max_label) # Max
    plt.axhline(y = min_val[0], color = "yellow", label = min_label) # Min

    plt.legend()

    plt.show()

def visualize_distribution(data_dict: dict, sorted = True) -> plt:

    x_axis = []
    y_axis = []

    if sorted: 

        while len(data_dict) > 0:

            max_key = max(data_dict, key = data_dict.get)
            max_val = data_dict[max_key]

            x_axis.append(max_key)
            y_axis.append(max_val)

            del data_dict[max_key]

    else:
        x_axis = list(data_dict.keys)
        y_axis = list(data_dict.values)

    fig = plt.figure(figsize = (10, 5))

    plt.bar(x_axis, y_axis)

    plt.show()