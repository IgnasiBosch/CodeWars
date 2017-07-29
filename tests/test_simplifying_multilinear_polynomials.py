from unittest import TestCase
from src.simplifying_multilinear_polynomials import simplify


class TestGapInPrimes(TestCase):
    def test_1(self):
        self.assertEqual("cd+abcd", simplify("dc+dcba"))

    def test_2(self):
        self.assertEqual("xy", simplify("2xy-yx"))

    def test_3(self):
        self.assertEqual("-c+5ab", simplify("-a+5ab+3a-c-2a"))

    def test_4(self):
        self.assertEqual("3a+2ac-abc", simplify("-abc+3a+2ac"))

    def test_5(self):
        self.assertEqual("-xz+xyz", simplify("xyz-xz"))

    def test_6(self):
        self.assertEqual("a-ab+ac", simplify("a+ca-ab"))

    def test_7(self):
        self.assertEqual("byz+xyz", simplify("xzy+zby"))

    def test_8(self):
        self.assertEqual("x-y", simplify("-y+x"))

    def test_9(self):
        self.assertEqual("-x+y", simplify("y-x"))
