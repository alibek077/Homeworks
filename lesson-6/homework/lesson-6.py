
# Task 1

txt = 'abcabcdabcdeabcdefabcdefg'
vowels = 'uiaeoAOIUE'
cnt = 2
while cnt < len(txt):
    if txt[cnt] not in vowels:
        txt = txt[:cnt+1] + '_' + txt[cnt +1:]
        vowels += txt[cnt]
        cnt = cnt + 4
        #continue
    cnt = cnt + 1
    
txt[:-1]
        


# Task2

n = int(input())
for i in range(n):
    print(i**2)





# Task 3


# Exercise 1
i = 1
while i <= 10:
    print(i)
    i += 1


# Exercise 2

n = int(input("Enter number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum is:", total)



# Exercise 3

n = int(input("Enter number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum is:", total)



# Exercise 4

n = int(input("Enter number: "))
for i in range(1, 11):
    print(n * i)



# Exercise 5

numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break
    if num > 100:
        print(num)



# Exercise 6

num = int(input())
print("Number of digits:", len(str(abs(num))))




# Exercise 7

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()




# Exercise 8

    list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)


# Exercise 9

for i in range(-10, 0):
    print(i)



# Exercise 10

for i in range(5):
    print(i)
print("Done!")





# Exercise 11

start, end = 25, 50
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            print(num)




# Exercise 12
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b





# Exercise 13
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"{n}! = {fact}")

