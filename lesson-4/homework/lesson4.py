#2
my_dict = {0: 10, 1: 20}

my_dict[2] = 30

print("Updated Dictionary:", my_dict)

n = 5


#4
squares_dict = {x: x*x for x in range(1, n+1)}

print(f'Squares Dictionary:" {squares_dict}')


#5
squares_dict = {x: x**2 for x in range(1, 16)}
print("Squares from 1 to 15:", squares_dict)



#1
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

#2
my_set = {10, 20, 30, 40}

print("Iterating over set:")
for item in my_set:
    print(item)


#3
my_set = {1, 2, 3}

my_set.add(4)

my_set.update([5, 6])

print("Updated Set:", my_set)



#4
my_set = {1, 2, 3, 4}

my_set.remove(2)

print("Set after removal:", my_set)


#5
my_set = {10, 20, 30, 40}

my_set.discard(20)

print("Set after discard:", my_set)

