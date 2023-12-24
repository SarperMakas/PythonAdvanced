"""python -m unittest test_calc.py"""

import unittest
import calc


class TestCalc(unittest.TestCase):

    def setUp(self):
        # before every test
        print("setUp")
    def tearDown(self):
        # after every test
        print("tearDown\n")

    def test_add(self):  # test method must start with test
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
        print("add")

    def test_subtract(self):  # test method must start with test
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)
        print("subtract")

    def test_multiply(self):  # test method must start with test
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
        print("multiply")

    def test_divide(self):  # test method must start with test
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # self.assertRaises(ValueError, calc.divide, 10, 0)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

        print("divide")


if __name__ == "__main__":
    unittest.main()
