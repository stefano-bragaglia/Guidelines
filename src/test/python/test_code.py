import csv
import os
from unittest import TestCase

from assertpy import assert_that

from code import func
from code import value

FIXTURES = os.path.join(os.path.dirname(__file__), '..', 'fixtures')


class CodeTest(TestCase):

    def test__value(self):
        for expected in [1, 1, 1]:
            with self.subTest(params=expected):
                result = value()

                assert_that(result, 'value').is_equal_to(expected)

    def test__func(self):
        with open(os.path.join(FIXTURES, 'data.csv'), 'r') as file:
            data = [(int(r['Value']), int(r['Expected'])) for r in csv.DictReader(file)]

        for i, expected in data:
            with self.subTest(i=i, expected=expected):
                result = func(i)

                assert_that(result, 'func').is_equal_to(expected)
