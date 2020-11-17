import math

class FunctionsProcessor:
    def __init__(self, list_a, list_b):
        """Initialize two lists of function data."""
        self.list_a = list_a
        self.list_b = list_b

    def compute_pearson_correlation(self):
        """The method compute pearson correlation and return it."""
        # compute the mean of list a and b
        mean_list_a = sum(self.list_a)/len(self.list_a)
        mean_list_b = sum(self.list_b)/len(self.list_b)

        # compute numerator of pearson correlation formula
        func_multiply = lambda a, b: (a - mean_list_a) * (b - mean_list_b)
        list_ab = list(map(func_multiply, self.list_a, self.list_b))
        numerator = sum(list_ab)
        # TODO: debug
        # print("numerator:", numerator)

        # compute denominator of pearson correlation formula
        sqrt_term_list_a = self.compute_sqrt_term(mean_list_a, self.list_a)
        sqrt_term_list_b = self.compute_sqrt_term(mean_list_b, self.list_b)
        denominator = sqrt_term_list_a * sqrt_term_list_b
        # TODO: debug
        # print("denominator:", denominator)
        return numerator/denominator

    def compute_sqrt_term(self, mean_list, list_num):
        """The method compute square root term of the pearson formula."""
        func = lambda n: (n - mean_list) ** 2
        list_square = list(map(func, list_num))
        list_square_sum = sum(list_square)
        return math.sqrt(list_square_sum)
