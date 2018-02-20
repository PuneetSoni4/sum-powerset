import pytest

import sum_powerset_using_combination as sum_powerset_py_file
#import sum_powerset_using_generator as sum_powerset_py_file
#import sum_powerset_using_binary_bits as sum_powerset_py_file
#import sum_powerset_using_recursion as sum_powerset_py_file
#import sum_powerset_using_logic as sum_powerset_py_file


# using python pytest fixture to create and destroy class object with function scope
@pytest.yield_fixture(scope="function", autouse=True)
def powerset_fixture(request):
    ''' Creating function fixture for testing Power-Set Sum '''

    powerset_object = sum_powerset_py_file.SUMPOWERSET()
    if request.cls is not None:
        request.cls.powerset_object = powerset_object
    yield powerset_object
    del powerset_object


# implementing fixture to complete test class
@pytest.mark.usefixtures('powerset_fixture')
class TestSumPowerSet(object):
    """ Test Class"""

    def test_sum_powerset_1(self):
        assert self.powerset_object.sum_powerset("") == 0

    def test_sum_powerset_2(self):
        assert self.powerset_object.sum_powerset("123") == 24

    def test_sum_powerset_3(self):
        assert self.powerset_object.sum_powerset("321") == 24

    def test_sum_powerset_4(self):
        assert self.powerset_object.sum_powerset("123") != 28

    def test_sum_powerset_5(self):
        assert self.powerset_object.sum_powerset("1234") == 80

    def test_sum_powerset_6(self):
        assert self.powerset_object.sum_powerset("abc") == -1

    def test_sum_powerset_7(self):
        assert self.powerset_object.sum_powerset("-123") == -1

    def test_sum_powerset_8(self):
        assert self.powerset_object.sum_powerset("1.23") == -1

    def test_sum_powerset_9(self):
        assert self.powerset_object.sum_powerset("12") == 6

    def test_sum_powerset_10(self):
        assert self.powerset_object.sum_powerset("12345") == 240

    def test_sum_powerset_11(self):
        assert self.powerset_object.sum_powerset("123456") == 672
