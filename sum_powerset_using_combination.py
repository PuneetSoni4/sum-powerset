from itertools import combinations

class SUMPOWERSET(object):
    """ Sum powerset class """

    def __init__(self):
        """ init method """
        self.result_list = []

    def sum_powerset(self, data):
        """ To generate and return sum of powerset elements of given data """

        try:
            # converting data to list
            data_list = list(data)

            # getting all possible combinations for given data list items
            for size in range(len(data_list) + 1):
                data_combinations = combinations(data_list, size)
                for element in data_combinations:
                    # extending result list to merge elements of data_combinations
                    self.result_list.extend(list(element))

            # converting/mapping every element of result_list to integer
            try:
                result_elements = list(map(int, self.result_list))
            except ValueError:
                return -1

            # returning sum of list elements
            return sum(result_elements)
        except Exception as exception:
            return "Caught exception. {0}".format(str(exception))
