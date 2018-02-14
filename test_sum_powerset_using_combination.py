import sum_powerset_using_combination as spuc

class TestSumPowerSet(object):

    def test_sum_powerset_1(self):
        assert spuc.sum_powerset("") == 0

    def test_sum_powerset_2(self):
        assert spuc.sum_powerset("123") == 24

    def test_sum_powerset_3(self):
        assert spuc.sum_powerset("321") == 24

    def test_sum_powerset_4(self):
        assert spuc.sum_powerset("123") != 28

    def test_sum_powerset_5(self):
        assert spuc.sum_powerset("1234") == 80

    def test_sum_powerset_6(self):
        assert spuc.sum_powerset("abc") == -1

    def test_sum_powerset_7(self):
        assert spuc.sum_powerset("-123") == -1

    def test_sum_powerset_8(self):
        assert spuc.sum_powerset("1.23") == -1
