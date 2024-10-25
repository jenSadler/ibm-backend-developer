"""Test the mymodule class"""

import unittest
from mymodule import square, double

class TestSquare(unittest.TestCase):
    """Test the square functions"""
    def test1(self):
        """First test - test squares with ints, floats and negatives"""
        self.assertEqual(square(2), 4)
        self.assertEqual(square(3.0), 9.0)
        self.assertNotEqual(square(-3), -9)


class TestDouble(unittest.TestCase):
    """Test doubles functions"""
    def test1(self):
        """Test doubling ints, floats and 0 """
        self.assertEqual(double(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(double(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2)
        self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.

unittest.main()
