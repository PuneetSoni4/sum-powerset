""" Currently supporting 'data' length of 4 integers """
""" TODO: support for more than 4 integers """
""" STATUS: IN PROGRESS """

class SUMPOWERSET(object):
    """ Sum powerset class """

    def __init__(self):
        """ init method """
        self.result_list = []

    def custom_combinations(self, data_list, size):
        """ Customised combination method """

        # params
        combinations_list = []

        for element in data_list:

            # getting index of element
            index_of_element = data_list.index(element)

            for next_element in data_list[index_of_element + 1:]:

                # adding first element to combinations_list
                combinations_list.append(element)

                # adding next elements to combinations_list
                combinations_list.append(next_element)

        return combinations_list

    def sum_powerset(self, data):
        """ To generate and return sum of powerset elements of given data """

        try:
            # converting data to list
            data_list = list(data)

            # adding individual elements of list to result_list
            self.result_list.extend(data_list)

            # getting all possible combinations for given data list items
            len_data_list = len(data_list)

            if len_data_list > 2:
                for size in range(2, len_data_list):
                    data_combinations = self.custom_combinations(data_list, size)
                    # extending result list to merge elements of data_combinations
                    self.result_list.extend(data_combinations)

            # adding individual elements of list to result_list again
            # as final combination will comprise of same elements
            self.result_list.extend(data_list)

            # converting/mapping every element of result_list to integer
            try:
                result_elements = list(map(int, self.result_list))
            except ValueError:
                return -1
            # returning sum of list elements
            return sum(result_elements)
        except Exception as exception:
            return "Caught exception. {0}".format(str(exception))
