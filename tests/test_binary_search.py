from unittest import TestCase
from src.binary_search import binary_search_recursive


class TestBinarySearch(TestCase):
    def test_1(self):
        _list = range(1001)
        self.assertTrue(binary_search_recursive(_list, 500))

    def test_2(self):
        _list = range(1001)
        self.assertTrue(binary_search_recursive(_list, 277))

    def test_3(self):
        _list = range(1001)
        self.assertFalse(binary_search_recursive(_list, 2770))

