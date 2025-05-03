import math

side = int(input('Enter the side length of the square: '))
square_perimeter = 4 * side
square_area = side ** 2
print('Perimeter of square:', square_perimeter)
print('Area of square: ', square_area)


diameter = int(input('Enter the diameter of the circle: '))
circumference = math.pi * diameter
print('Circumference of circle:' ,circumference)


a = int(input('Enter the first number (a): '))
b = int(input('Enter the second number (b): '))
mean = (a + b) / 2
print(f'Mean of {a} and {b}: {mean}')

sum = a + b
product = a * b
square_a = a ** 2
square_b = b ** 2
print(f'Sum of {a} and {b}: {sum}')
print(f'Product of {a} and {b}: {product}')
print(f'Square of {a}: {square_a}')
print(f'Square of {b}: {square_b}')
