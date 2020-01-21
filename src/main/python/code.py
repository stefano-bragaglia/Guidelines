import csv
import os

FIXTURES = os.path.join(os.path.dirname(__file__), '..', 'fixtures')


def value() -> int:
    with open(os.path.join(FIXTURES, 'data.csv'), 'r') as file:
        for record in csv.DictReader(file):
            try:
                return int(record.get('Value', '0'))

            except ValueError:
                return 0

    return 0


def func(x: int = 0) -> int:
    return x
