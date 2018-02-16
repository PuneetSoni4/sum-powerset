class SUMPOWERSET(object):
    """ Sum powerset class """

    def __init__(self):
        """ init method """
        self.result_list = []

    def custom_combinations_binary(self, data_list):
        """ To generate combinations of given data_list using binary """

        # params
        combinations_list = []
        counter = 0
        element_counter = 0
        length_of_data_list = len(data_list)

        # powerset size
        powerset_size = pow(2, length_of_data_list)

        for counter in range(powerset_size):
            for element_counter in range(length_of_data_list):
                if counter & (1<<element_counter):
                    combinations_list.append(data_list[element_counter])

        return combinations_list


    def sum_powerset(self, data):
        """ To generate and return sum of powerset elements of given data """

        try:
            # converting data to list
            data_list = list(data)

            self.result_list = self.custom_combinations_binary(data_list)

            # converting/mapping every element of result_list to integer
            try:
                result_elements = list(map(int, self.result_list))
            except ValueError:
                return -1
            # returning sum of list elements
            return sum(result_elements)
        except Exception as exception:
            return "Caught exception. {0}".format(str(exception))
