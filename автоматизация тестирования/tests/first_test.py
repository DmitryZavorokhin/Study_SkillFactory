import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculator_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculator_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5
