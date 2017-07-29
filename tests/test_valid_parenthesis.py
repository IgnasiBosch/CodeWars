from unittest import TestCase
from src.valid_parenthesis import valid_parentheses


class TestValidParenthesis(TestCase):
    def test_basic_tests_false(self):
        self.assertFalse(valid_parentheses(')'))
        self.assertFalse(valid_parentheses('('))
        self.assertFalse(valid_parentheses('hi)('))
        self.assertFalse(valid_parentheses('hi(hi)('))
        self.assertFalse(valid_parentheses('hi(hi))('))

    def test_basic_tests_true(self):
        self.assertTrue(valid_parentheses(''))
        self.assertTrue(valid_parentheses('hi(hi)'))
        self.assertTrue(valid_parentheses('((())()())'))
        self.assertTrue(valid_parentheses('(c(b(a)))(d)'))
