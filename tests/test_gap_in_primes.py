from unittest import TestCase
from src.gap_in_primes import gap


class TestGapInPrimes(TestCase):
    def test_1(self):
        expected_result = [101, 103]
        self.assertEqual(expected_result, gap(2, 100, 110))

    def test_2(self):
        expected_result = [103, 107]
        self.assertEqual(expected_result, gap(4, 100, 110))

    def test_3(self):
        expected_result = None
        self.assertEqual(expected_result, gap(6, 100, 110))

    def test_4(self):
        expected_result = [359, 367]
        self.assertEqual(expected_result, gap(8, 300, 400))

    def test_5(self):
        expected_result = [337, 347]
        self.assertEqual(expected_result, gap(10, 300, 400))

    def test_6(self):
        expected_result = [30109, 30113]
        self.assertEqual(expected_result, gap(4, 30000, 100000))

    def test_7(self):
        expected_result = [30091, 30097]
        self.assertEqual(expected_result, gap(6, 30000, 100000))

    def test_8(self):
        expected_result = [30161, 30169]
        self.assertEqual(expected_result, gap(8, 30000, 100000))

    def test_9(self):
        expected_result = None
        self.assertEqual(expected_result, gap(11, 30000, 100000))

    def test_10(self):
        expected_result = [10000139, 10000141]
        self.assertEqual(expected_result, gap(2, 10000000, 11000000))
