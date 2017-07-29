from unittest import TestCase
from src.find_the_missing_term_in_an_arithmetic_progression import find_missing


class TestGapInPrimes(TestCase):
    def test_1(self):
        expected_result = 5
        self.assertEqual(expected_result, find_missing([1, 2, 3, 4, 6, 7, 8, 9]))

    def test_11(self):
        expected_result = 2
        self.assertEqual(expected_result, find_missing([1, 3, 4, 5, 6, 7, 8, 9]))

    def test_2(self):
        expected_result = 7
        self.assertEqual(expected_result, find_missing([1, 3, 5, 9, 11]))

    def test_3(self):
        expected_result = -7
        self.assertEqual(expected_result, find_missing([-1, -3, -5, -9, -11]))

    def test_4(self):
        expected_result = 140
        self.assertEqual(expected_result, find_missing([100, 110, 120, 130, 150]))
