class SUMPOWERSET(object):
    """ Sum powerset class """

    def __init__(self):
        """ init method """
        self.result_list = []

    def custom_combinations_generator(self, data_string):
        """ custom combination generator"""

        # the first value returned is empty
        yield ''

        for pos, data in enumerate(data_string):
            for combination in self.custom_combinations_generator(data_string[pos + 1:]):
                yield data + combination

    def sum_powerset(self, data):
        """ To return sum of elements of power-set of given data string """

        try:
            # getting result list with all combinations of given data string
            result = self.custom_combinations_generator(data)

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
