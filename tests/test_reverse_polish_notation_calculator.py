from unittest import TestCase
from src.reverse_polish_notation_calculator import calc


class TestGapInPrimes(TestCase):
    def test_1(self):
        self.assertEqual(0, calc(""))

    def test_2(self):
        self.assertEqual(3, calc("1 2 3"))

    def test_3(self):
        self.assertEqual(3.5, calc("1 2 3.5"))

    def test_4(self):
        self.assertEqual(4, calc("1 3 +"))

    def test_5(self):
        self.assertEqual(3, calc("1 3 *"))

    def test_6(self):
        self.assertEqual(-2, calc("1 3 -"))

    def test_7(self):
        self.assertEqual(2, calc("4 2 /"))

    def test_8(self):
        self.assertEqual(14, calc("5 1 2 + 4 * + 3 -"))


