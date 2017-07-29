from unittest import TestCase
from src.finding_an_appointment import get_start_time


class TestGapInPrimes(TestCase):

    schedules = [
        [['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']],
        [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
        [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]
    ]

    def test_1(self):
        self.assertEqual('12:15', get_start_time(self.schedules, 60))

    def test_2(self):
        self.assertEqual(None, get_start_time(self.schedules, 90))

