import unittest
from lab1 import calculate_square, calculate_cube

class TestFunctions(unittest.TestCase):

    def test_calculate_square(self):
        self.assertEqual(calculate_square(2), 4)
        self.assertEqual(calculate_square(3), 9)
        self.assertEqual(calculate_square(0), 0)

    def test_calculate_cube(self):
        self.assertEqual(calculate_cube(2), 8)
        self.assertEqual(calculate_cube(3), 27)
        self.assertEqual(calculate_cube(0), 0)


unittest.main()
