# Functional Programming
from cv2 import multiply


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)

    return new_list


print(multiply_by2([1, 2, 3]))

# map, filter, zip and reduce
# map()
my_list = [1, 2, 3]


def multiply_by2(items):
    return items*2


print(list(map(multiply_by2, my_list)))
print(my_list)

# filter()
def check_odd(item):
    return item % 2 != 0

print(list(filter(check_odd, my_list)))

# zip()
your_list = [10,20,30]
their_list = (5,15,25)
print(list(zip(my_list, your_list, their_list)))

# reduce()
from functools import reduce

def accumulator(acc, item):
    print(acc, item)
    return acc + item
    
print(reduce(accumulator, my_list, 0))

# Exercise
#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize(string):
    return string.upper()

print(list(map(capitalize, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def find(num):
    return num > 50

print(list(filter(find, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def sum(acc, item):
    print(acc, item)
    return acc + item

print(reduce(sum, (my_numbers + scores)))

# lambda expressions
lambda param : action(param)
print(list(map(lambda item: item * 2, my_list))) # when you are using the function only one time.
print(list(filter(lambda item:item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc + item, my_list))

# Exercise
# square
my_list = [5,4,3]

print(list(map(lambda item: item ** 2, my_list)))

# List Sorting
a = [(0,2), (4,3),(9,9),(10,-1)]
a.sort(key = lambda x:x[1])
print(a)
# print(list(filter(lambda item:item)))

# Comprehensions: list, set, dictionary
my_list = [char for char in 'hello']
my_list2 = [num for num in range(0,100)]
my_list3 = [num*2 for num in range(0,100)]
my_list4 = [num**2 for num in range(0,100) if num%2 == 0]

for char in 'hello':
    my_list.append(char)

print(my_list4)

# set comprehensions
my_list = {char for char in 'hello'}
my_list2 = {num for num in range(0,100)}
my_list3 = [num*2 for num in range(0,100)]
my_list4 = {num**2 for num in range(0,100) if num%2 == 0}

print(my_list4)

# dictionary comprehensions
simple_dict = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}
my_dict = {key:value**2 for key,value in simple_dict.items() }
print(my_dict)

# Exercise
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'c']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
            
print(duplicates)