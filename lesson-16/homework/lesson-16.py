#1
import numpy as np

original_list = [12.23, 13.32, 100, 36.32]
array_1d = np.array(original_list)
print("Original List:", original_list)
print("One-dimensional NumPy array:", array_1d)

#2
matrix_3x3 = np.arange(2, 11).reshape(3, 3)
print("3x3 Matrix:")
print(matrix_3x3)

#3
null_vector = np.zeros(10)
print("Null Vector:", null_vector)
null_vector[6] = 11
print("Updated Vector:", null_vector)

#4
array_12_38 = np.arange(12, 38)
print("Array from 12 to 38:")
print(array_12_38)

#5
original_array = np.array([1, 2, 3, 4])
float_array = original_array.astype(float)
print("Original array:")
print(original_array)
print("Array as float:")
print(float_array)

#6
celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit = celsius * 9/5 + 32
print("Values in Centigrade degrees:")
print(celsius)
print("Values in Fahrenheit degrees:")
print(fahrenheit)

#7
original_array = np.array([10, 20, 30])
new_values = np.array([40, 50, 60, 70, 80, 90])
combined_array = np.append(original_array, new_values)
print("Original array:")
print(original_array)
print("After appending values:")
print(combined_array)

#8
random_array = np.random.rand(10)
mean = np.mean(random_array)
median = np.median(random_array)
std_dev = np.std(random_array)
print("Random array:", random_array)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)

#9
array_10x10 = np.random.rand(10, 10)
min_val = np.min(array_10x10)
max_val = np.max(array_10x10)
print("10x10 Random Array:")
print(array_10x10)
print("Minimum Value:", min_val)
print("Maximum Value:", max_val)

#10
array_3x3x3 = np.random.rand(3, 3, 3)
print("3x3x3 Random Array:")
print(array_3x3x3)
