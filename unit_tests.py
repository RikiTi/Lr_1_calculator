# Module for work with tests and check how work calculator
import sys
import unittest
from unittest import TestCase
from unittest.mock import patch, Mock
from math import inf


class TestCalculator(TestCase):
    # class for create and run with tests

    @patch(target='calculators.EconomicalCalculator.addition', return_value=164)
    def test_easy_addition(self, func):
        """Method for test and check addition function with normal numbers"""
        answer = func(24, 140)
        self.assertAlmostEqual(answer, 164)

    @patch(target='calculators.EconomicalCalculator.addition', return_value=inf)
    def test_hard_addition(self, func):
        """Method for test and check addition function with max numbers"""
        answer = func(inf, sys.maxsize)
        self.assertAlmostEqual(answer, inf)

    @patch(target='calculators.EconomicalCalculator.division', return_value=2.25)
    def test_division(self, func):
        """Method for test and check division function"""
        answer = func(9, 14)
        self.assertAlmostEqual(answer, 2.25)


if __name__ == "__main__":
    unittest.main()
