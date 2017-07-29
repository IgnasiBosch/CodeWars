from unittest import TestCase
from src.pete_the_baker import cakes


class TestPeteTheBaker(TestCase):
    def test_basic_recipe_1(self):
        recipe = {"flour": 500, "sugar": 200, "eggs": 1}
        available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
        expected_result = 2
        self.assertEqual(expected_result, cakes(recipe, available))

    def test_basic_recipe_2(self):
        recipe = {"cream": 200, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
        available = {"sugar": 1700, "flour": 20000, "milk": 20000, "oil": 30000, "cream": 5000}
        expected_result = 11
        self.assertEqual(expected_result, cakes(recipe, available))

    def test_missing_ingredient_1(self):
        recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
        available = {"sugar": 500, "flour": 2000, "milk": 2000}
        expected_result = 0
        self.assertEqual(expected_result, cakes(recipe, available))

    def test_not_enough_ingredients(self):
        recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
        available =  {"sugar": 500, "flour": 2000, "milk": 2000, "apples": 15, "oil": 20}
        expected_result = 0
        self.assertEqual(expected_result, cakes(recipe, available))

    def test_not_ingredients_available(self):
        recipe = {"eggs": 4, "flour": 400}
        available = {}
        expected_result = 0
        self.assertEqual(expected_result, cakes(recipe, available))

    def test_exactly_enough_ingredients_for_1_cake(self):
        recipe = {"cream": 1, "flour": 3, "sugar": 1, "milk": 1, "oil": 1, "eggs": 1}
        available = {"sugar": 1, "eggs": 1, "flour": 3, "cream": 1, "oil": 1, "milk": 1}
        expected_result = 1
        self.assertEqual(expected_result, cakes(recipe, available))