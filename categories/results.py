from math_stats import MathStats

class Results():

    def __init__(self):

        self.logic = None
        self.math = MathStats()

    def basic_analysis(self):

        self.math.calc_all_values()

    def get_results(self):
        pass

    