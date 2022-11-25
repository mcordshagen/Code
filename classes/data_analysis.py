import pandas as pd

from classes.data_processing import DataProcessing
from categories.math_stats import MathStats
from categories.free_of_error import FreeOfError
from categories.relevancy import Relevancy
from categories.completeness import Completeness

class DataAnalysis(DataProcessing):

    def __init__(self):

        super().__init__()

        self.mathstats = MathStats()
        self.free_of_error = FreeOfError()
        self.relevancy = Relevancy()
        self.completness = Completeness()


    def list_of_numeric_columns(self):

        self.numeric_columns = []

        for column in self.data:

            if pd.api.types.is_numeric_dtype(self.data[column]):
                self.numeric_columns.append(column)

    def basic_anylsis(self):

        self.list_of_numeric_columns()
        self.mathstats.calc_all_values(self.data, self.numeric_columns)

        self.free_of_error.format_analysis(self.data)
        self.free_of_error.check_lengths(self.data)

        self.relevancy.check_relevancy(self.data)
        self.relevancy.inferences_all(self.data)

        self.completness.create_column_dicts(self.data)

    def results_basic_analysis(self, math_stats = True, relevancy = True, lengths = True, formats = True, column_dicts = False) -> None:

        if math_stats: self.mathstats.print_math_stats()
        
        if relevancy: self.relevancy.print_relevancy()

        if lengths: self.free_of_error.print_lengths()
        if formats: self.free_of_error.print_formats()
        
        if column_dicts: self.completness.print_column_dicts()
        
