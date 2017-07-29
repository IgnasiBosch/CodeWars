from unittest import TestCase
from src.primes_in_numbers import prime_factors


class TestGapInPrimes(TestCase):
    def test_1(self):
        expected_result = '(2**5)(5)(7**2)(11)'
        self.assertEqual(expected_result, prime_factors(86240))

    def test_2(self):
        expected_result = '(2**2)(3**3)(5)(7)(11**2)(17)'
        self.assertEqual(expected_result, prime_factors(7775460))

    def test_3(self):
        expected_result = '(7919)'
        self.assertEqual(expected_result, prime_factors(7919))

    def test_4(self):
        expected_result = '(3**3)(28798037)'
        self.assertEqual(expected_result, prime_factors(777546999))
