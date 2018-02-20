class SUMPOWERSET(object):
    """ Sum powerset class """

    def __init__(self):
        """ init method """
        self.result_list = []

    def custom_combinations_recursive(self, data_list):
        """ To generate combinations of given data_list recursively """

        # params
        combinations_list = []

        if data_list:
            head, tail = data_list[:1], data_list[1:]
            for smaller in self.custom_combinations_recursive(tail):
                combinations_list.append(smaller)
                combinations_list.append(head + smaller)
        else:
            combinations_list.append([])

        return combinations_list


    def sum_powerset(self, data):
        """ To generate and return sum of powerset elements of given data """

        try:
            # converting data to list
            data_list = list(data)

            result = self.custom_combinations_recursive(data_list)

            # extending result_list with elements of result
            for element in result:
                self.result_list.extend(element)

            # converting/mapping every element of result_list to integer
            try:
                result_elements = list(map(int, self.result_list))
            except ValueError:
                return -1
            # returning sum of list elements
            return sum(result_elements)
        except Exception as exception:
            return "Caught exception. {0}".format(str(exception))
