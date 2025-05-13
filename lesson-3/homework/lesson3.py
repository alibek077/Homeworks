#1
fruits = ['apple', 'banana', 'cherry', 'orange', 'grape']
print(f'third fruit: {fruits[0]}')

#2
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(f'Concatenated list: {combined_list}')

#3
numbers = [1, 3, 5, 9, 10, 11, 19]
middle_number = len(numbers) // 2
extracted_numbers = [numbers[0], numbers[middle_number], numbers[-1]]
print(f'Extracted numbers: {extracted_numbers}')


#4
favorite_movies = ['Marvel', 'Interstellar', 'Boyka', 'Pablo Escobar', 'Titanic']
movies_tuple = tuple(favorite_movies)
print(f'Movies tuple: {movies_tuple}')


#5
cities = ['London', 'New York', 'Paris', 'Tokyo']
print(f'Is Paris in the list? {'Paris' in cities}')


#6
nums = [1, 2, 3]
duplicated = nums * 2
print(f'Duplicated list: {duplicated}')

#7
swap_list = [11, 22, 33, 44, 55]
swap_list[0], swap_list[-1] = swap_list[-1], swap_list[0]
print(f'Swapped list: {swap_list}')


#8
num_tuple = tuple(range(1, 10))
sliced = num_tuple[3:7] 
print(f'Sliced tuple: {sliced}')


#9
colors = ['blue', 'red', 'blue', 'green', 'blue', 'yellow']
count = colors.count('blue')
print(f'Blue count: {count}')


#10
animals = ('cat', 'dog', 'lion', 'tiger', 'elephant')
index = animals.index('lion')
print(f'Index of "lion": {index}')

#11
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print(f'Merged tuple: {merged_tuple}')



#12
sample_list = [10, 20, 30]
sample_tuple = (100, 200, 300, 400)
print(f'Length of list: {len(sample_list)}')
print(f'Length of tuple: {len(sample_tuple)}')




#13


#14
tuple = (1, 20, 15, 30, 10, 77)
print(f'Maximum: {max(tuple)}')
print(f'Minimum: {min(tuple)}')


#15
words = ('hello', 'Ali', 'python', 'Maab', 'wiut')
reversed_tuple = words[::-1]
print(f'Reversed tuple: {reversed_tuple}')
