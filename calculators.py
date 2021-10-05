"""Module for implementation math operations in different calculators"""
from math_operations.addition import AdditionInterface
from math_operations.division import DivisionInterface
from math_operations.subtraction import SubtractionInterface
from math_operations.multiplication import MultiplicationInterface


class EngineeringCalculator(AdditionInterface, SubtractionInterface, DivisionInterface, MultiplicationInterface):
    """Class for realization functional of engineering calculator"""

    def addition(self, first_value, second_value):
        """Method for realization an addition operation and return bytes type"""
        return bytes(first_value + second_value)

    def subtraction(self, first_value, second_value):
        """Method for realization subtraction operation"""
        return bytes(first_value - second_value)

    def division(self, first_value, second_value):
        """Method for realization division operation"""
        return bytes(first_value / second_value)

    def multiplication(self, first_value, second_value):
        """Method for realization multiplication operation"""
        return bytes(first_value * second_value)


class EconomicalCalculator(AdditionInterface, SubtractionInterface, DivisionInterface, MultiplicationInterface):
    """Class for realization functional of economical calculator"""

    def addition(self, first_value, second_value):
        """Method for realization an addition operation"""
        return first_value + second_value

    def subtraction(self, first_value, second_value):
        """Method for realization subtraction operation"""
        return first_value - second_value

    def division(self, first_value, second_value):
        """Method for realization division operation"""
        return first_value / second_value

    def multiplication(self, first_value, second_value):
        """Method for realization multiplication operation"""
        return first_value * second_value
