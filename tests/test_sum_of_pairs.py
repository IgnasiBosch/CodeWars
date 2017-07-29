from unittest import TestCase
from src.sum_of_pairs import sum_pairs


class TestGapInPrimes(TestCase):
    def test_1(self):
        ints = [1, 4, 8, 7, 3, 15]
        expected_result = [1, 7]
        self.assertListEqual(expected_result, sum_pairs(ints, 8))

    def test_2(self):
        ints = [1, -2, 3, 0, -6, 1]
        expected_result = [0, -6]
        self.assertListEqual(expected_result, sum_pairs(ints, -6))

    def test_3(self):
        ints = [20, -13, 40]
        expected_result = None
        self.assertEquals(expected_result, sum_pairs(ints, -7))

    def test_4(self):
        ints = [1, 2, 3, 4, 1, 0]
        expected_result = [1, 1]
        self.assertEquals(expected_result, sum_pairs(ints, 2))

    def test_5(self):
        ints = [10, 5, 2, 3, 7, 5]
        expected_result = [3, 7]
        self.assertEquals(expected_result, sum_pairs(ints, 10))

    def test_6(self):
        ints = [4, -2, 3, 3, 4]
        expected_result = [4, 4]
        self.assertEquals(expected_result, sum_pairs(ints, 8))

    def test_7(self):
        ints = [0, 2, 0]
        expected_result = [0, 0]
        self.assertEquals(expected_result, sum_pairs(ints, 0))

    def test_8(self):
        ints = [5, 9, 13, -3]
        expected_result = [13, -3]
        self.assertEquals(expected_result, sum_pairs(ints, 10))
