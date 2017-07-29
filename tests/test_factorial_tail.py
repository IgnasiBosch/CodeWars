from unittest import TestCase
from src.factorial_tail import zeroes


class TestGapInPrimes(TestCase):
    def test_1(self):
        self.assertEqual(2, zeroes(10, 10))

    def test_2(self):
        self.assertEqual(3, zeroes(16, 16))

"""
test.assert_equals(zeroes(10, 10), 2, "10! has 2 zeroes in decimal")
test.assert_equals(zeroes(16, 16), 3, "0x10! has 3 zeroes in hexadecimal")
"""