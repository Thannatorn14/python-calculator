import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(3, 4), 7)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(11, 1), 10)
        self.assertEqual(self.calc.subtract(7, 2), 5)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(8, 9), 72)
        self.assertEqual(self.calc.multiply(7, 8), 56)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(12, 2), 6)
        self.assertEqual(self.calc.divide(100, 10), 10)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)
        self.assertEqual(self.calc.modulo(10, 3), 1)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()
