"""Module for implementation bases math operations in different calculators"""
from math_operations.addition import AdditionInterface
from math_operations.division import DivisionInterface
from math_operations.subtraction import SubtractionInterface
from math_operations.multiplication import MultiplicationInterface


class EngineeringCalculator(AdditionInterface, SubtractionInterface, DivisionInterface, MultiplicationInterface):
    """Class for realization functional of engineering calculator"""
    pass
