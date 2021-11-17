# Module for work with tests and check how work calculator
import sys
import unittest
from unittest import TestCase
from calculators import EconomicalCalculator
from math import inf


class TestCalculator(TestCase):
    # class for create and run with tests
    def setUp(self):
        self.base_calculator = EconomicalCalculator()

    def test_easy_addition(self):
        """Method for test and check addition function with normal numbers"""
        answer = self.base_calculator.addition(24, 140)
        self.assertAlmostEqual(answer, 164)

    def test_hard_addition(self):
        """Method for test and check addition function with max numbers"""
        answer = self.base_calculator.addition(inf, sys.maxsize)
        self.assertAlmostEqual(answer, inf)

    def test_division(self):
        """Method for test and check division function with exception"""
        with self.assertRaises(ZeroDivisionError):
            self.base_calculator.division(9, 0)


if __name__ == "__main__":
    unittest.main()
