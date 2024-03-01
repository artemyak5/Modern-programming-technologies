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


main()