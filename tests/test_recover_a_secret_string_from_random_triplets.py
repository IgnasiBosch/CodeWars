from unittest import TestCase
from src.recover_a_secret_string_from_random_triplets import recover_secret


class TestValidParenthesis(TestCase):
    def test_basic_tests_false(self):
        secret = "whatisup"
        triplets = [
            ['t', 'u', 'p'],
            ['w', 'h', 'i'],
            ['t', 's', 'u'],
            ['a', 't', 's'],
            ['h', 'a', 'p'],
            ['t', 'i', 's'],
            ['w', 'h', 's']
        ]
        self.assertEqual(secret, recover_secret(triplets))

