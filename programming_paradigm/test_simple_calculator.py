# programming_paradigm/test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6, places=7)

    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3, places=7)

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-3, 6), -18)
        self.assertEqual(self.calc.multiply(-3, -6), 18)
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0, places=7)

    def test_divide(self):
        """Test the divide method, including divide-by-zero behavior (returns None)."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0, places=7)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        # Edge cases: division by zero should return None per spec
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))


if __name__ == "__main__":
    unittest.main()
