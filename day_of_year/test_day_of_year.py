#!/usr/bin/env python3

import unittest
import json

from day_of_year import day_of_year


class TestDayOfYear(unittest.TestCase):

    def test_day_of_year(self):
        with open('test_data.json', 'r') as f:
            test_data = json.load(f)

        for test_k, test_v in test_data.items():
            self.assertEqual(day_of_year(test_v['year'], test_v['month'], test_v['day']),
                             test_v['result'],
                             test_v['msg'])


if __name__ == '__main__':
    unittest.main()
