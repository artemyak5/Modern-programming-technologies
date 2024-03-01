import unittest

def get_input():
    
    user_input = input("Введіть число: ")
    return float(user_input)


def calculate_square(number):
   
    square = number ** 2
    return square


def calculate_cube(number):

    cube = number ** 3
    return cube


def main():
    
    number = get_input()
    square = calculate_square(number)
    cube = calculate_cube(number)
    
    print(f"Квадрат числа {number} дорівнює: {square}")
    print(f"Куб числа {number} дорівнює: {cube}")


class TestFunctions(unittest.TestCase):

    def test_calculate_square(self):
        self.assertEqual(calculate_square(2), 4)
        self.assertEqual(calculate_square(3), 9)
        self.assertEqual(calculate_square(0), 0)

    def test_calculate_cube(self):
        self.assertEqual(calculate_cube(2), 8)
        self.assertEqual(calculate_cube(3), 27)
        self.assertEqual(calculate_cube(0), 0)


main()
unittest.main()