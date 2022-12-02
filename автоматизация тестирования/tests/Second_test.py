import pytest
from app.calculator import Calculator

class TestCalcr:
    def setup(self):
        self.Calc = Calculator

    def test_umnoj(self):
        assert self.Calc.multiply(self, 2, 3) == 6

    def test_minus(self):
        assert self.Calc.subtraction(self, 2, 2) == 0

    def test_delit(self):
        assert self.Calc.division(self, 2, 2) == 1

    def test_slojit(self):
        assert self.Calc.adding(self, 2, 3) == 5
