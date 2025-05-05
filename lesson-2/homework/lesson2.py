# 1
name = input('Enter your name:')
birth_year = int(input('Enter your birth year: '))
age = 2025 - birth_year
print(f'{name}, you are {age} years old.')

# 2
txt = 'LMaasleitbtui'
car_name = txt[::2] 
print(f'car name: {car_name}')

# 3
txt = 'MsaatmiazD'
car_name = txt[::2]
print('car name:', (car_name))

# 5
user_input = input('Enter a string: ')        
reversed_string = user_input[::-1]            
print('Reversed string:', reversed_string)

# 6
text = input('Enter a string: ')
vowels = "abcdefgABCDEFG"                             
count = 0
for char in text:                                
    if char in vowels:
        count += 1                                
print(f'Number of vowels: {count}')


# 7
numbers = input('Enter numbers separated by spaces: ')
num_list = [int(x) for x in numbers.split()]      
max_value = max(num_list)                     
print(f'Maximum value: {max_value}')


# 8
word = input('Enter a word: ')
if word == word[::-1]:                  
    print('It's a palindrome!')
else:
    print('Not a palindrome.')



# 9
email = input('Enter your email address: ')
domain = email.split('@')[1]           
print(f'Email domain: {domain}')
 

# 10
import random
import string

letters = string.ascii_letters
digits = string.digits

all_num = letters + digits

password = ''.join(random.sample(all_num, 12))
print(f'Generated password: {password}')
