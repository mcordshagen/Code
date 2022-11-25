class Outlier():

    def __init__(self):

        self.outlier_dict = {}
        self.max = None
        self.min = None
        self.avg = None


    def add_outlier(self, index, value):

        if index in self.outlier_dict:
            print(f"index {index} already in outlier_dict value: {value}")
        
        else:
            self.outlier_dict[index] = value

    def print_outlier(self, num = False):

        if num:

            self.max = max(self.outlier_dict)
            self.min = min(self.outlier_dict)
            self.avg = sum(self.outlier_dict.values()) / len(self.outlier_dict)
            print(f"max: {self.max} min: {self.min} avg: {self.avg}")

        print(f"outlier_dict: {self.outlier_dict}")
    