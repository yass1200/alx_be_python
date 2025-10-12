
import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Create a SimpleCalculator before each test."""
        self.calc = SimpleCalculator()

    # ---- add ----
    def test_add_integers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_add_floats(self):
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)
        self.assertAlmostEqual(self.calc.add(-0.5, 0.2), -0.3, places=7)

    def test_add_commutative(self):
        self.assertEqual(self.calc.add(10, 4), self.calc.add(4, 10))

    # ---- subtract ----
    def test_subtract_integers(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_subtract_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)
        self.assertAlmostEqual(self.calc.subtract(-1.25, 0.75), -2.0)

    def test_subtract_not_commutative(self):
        self.assertNotEqual(self.calc.subtract(9, 4), self.calc.subtract(4, 9))

    # ---- multiply ----
    def test_multiply_integers(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-3, 6), -18)
        self.assertEqual(self.calc.multiply(-3, -6), 18)
        self.assertEqual(self.calc.multiply(100000, 0), 0)

    def test_multiply_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0)
        self.assertAlmostEqual(self.calc.multiply(-1.2, 0.5), -0.6)

    def test_multiply_commutative(self):
        self.assertEqual(self.calc.multiply(7, 11), self.calc.multiply(11, 7))

    # ---- divide ----
    def test_divide_normal_integers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)

    def test_divide_floats(self):
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.divide(1, 4), 0.25)

    def test_divide_by_zero_returns_none(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_divide_signs(self):
        self.assertLess(self.calc.divide(-10, 2), 0)   # negative / positive -> negative
        self.assertGreater(self.calc.divide(-10, -2), 0)  # negative / negative -> positive


if __name__ == "__main__":
    unittest.main()
