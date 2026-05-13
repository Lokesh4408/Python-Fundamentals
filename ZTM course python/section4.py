import numpy as np

# Conditional logic
is_old = False
is_lincensed = False

if is_old:
    print('You are old enough to drive.')

elif is_lincensed:
    print('You have a valid license! you can go now')

else:
    print('You don\'t have a valid license, you faked it. So you are under arrest.')

print(bool('hello'))  # Truthy
print(bool(''))    # Falsely


# Ternary Operator
# condition_if_true if condition else condition_if_else
is_friend = False
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)

# Short Circuiting
is_friend = True
is_user = True

if is_friend or is_user:
    print('best friends forever')

# Logical operators: <, >, =
print(4 > 5)
print(4 == (8/2))
print('a' > 'b')  # here comparison of ASCII values take place
print(not(True))  # using not keyword as a function

is_magician = True
is_expert = False
# check if magician AND expert: 'you are a master magician'
if is_magician and is_expert:
    print('you are a master magician')
# check if magician but not expert: 'at least you're getting there'
elif is_magician and not(is_expert):
    print("at least you're getting there")
# if you're not a magician: 'you need magic powers'
elif not(is_magician):
    print('you need magic powers')

# is vs ==
print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)  # output is true
print([] == [])
print('\n')
print(True is True)
print('1' is '1')
print([] is [])  # 2 different lists at different places in memory
print(10 is 10)
print([1, 2, 3] is [1, 2, 3])

# For loops
for item in 'Zero to Mastery':
    print(item)

for item in {1, 2, 3, 4, 5}:
    print(item)

for item in (1, 2, 3, 4, 5):
    for x in ['a', 'b', 'c']:
        print(item, x)

# Iterables- list, dictionary, tuple, set, string
# Iterated: one by one check each item in the collection
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swin': False
}

for k, v in user.items():
    #key, value = item
    print(k, v)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

# for item in 50: # this gives a typeError saying int object is not iterable, coz 50 can't be iterated.
#     print(item)

# Tricky counter
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in my_list:
    sum = sum + i
print('Total sum of the list:', sum)

# range()
print(range(100))
for i in range(0, 10, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)

for _ in range(2):
    print(list(range(10)))

# enumerate
for i, char in enumerate('Helloo'):
    print(i, char)

for i, char in enumerate([1, 2, 3, 4, 5]):
    print(i, char)

for i, char in enumerate(list(range(10))):
    print(5, char)
    if char == 5:
        print(f'index of 50 is: {i}')


# while loops: infinite loops
j = 0
while j < 20:
    print(j)
    j = j + 1
    # break
else:   # else only works without break statement in a while loop
    print(f'done printing till {j}')

# while True:
#     response = input('say something: ')
#     if response == 'bye':
#         break


# break, continue, pass
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in my_list:
    sum = sum + i
    continue
    print(i)

while sum < len(my_list) + 55:
    pass
    print(sum)
    break
    # continue

for item in my_list:
    # thinking about it, don't bug me for a while
    pass

# our First GUI
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
print(f'{picture[2][2]} \n')

value = [[0] * 7] * 6  # np.array([np.zeros(6,7)])
print('value with zeros:', value)
for i in range(6):
    for k in range(7):
        if picture[i][k] == 0:
            print(' ', end='')
            # print(value[i][k])
        elif picture[i][k] == 1:
            print('*', end='')
            # print(value[i][k])
    print('')

# 1 iterate over picture: solution
for row in picture:
    for pixel in row:
        if (pixel == 1):  # if pixel:
            print('*', end='')
        else:
            print(' ', end='')
    print('')
# 2 if 0: print ' '
# 3 if 1: print *


# clean, readability, predictability and DRY: do not repeat yourself


# Find duplicates in list: Exercise problem
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

# Functions


def say_hello():
    print('Helloyo')


say_hello()


def show_tree():
    for row in picture:
        for pixel in row:
            if (pixel == 1):  # if pixel:
                print('*', end='')
            else:
                print(' ', end='')
        print('')


show_tree()
show_tree()
show_tree()
print(show_tree)


# positional Parameters
# default parameters
def say_hello(name='kavya', emoji=':)'):
    print(f'hellllooooo {name} {emoji}')


# positional Arguments
say_hello('Lokesh', ';)')
say_hello('Erik', ':D')


# Default parameters and Keyword arguments
say_hello(name='Lokesh', emoji=';)')  # don't use this kind without order
say_hello()


# return: it exits automatically from a function
def sum2(num1, num2):
    return num1+num2


total = sum2(10, 5)
# a function should do something really well and should return something.
print(sum2(11, total))


def sum_of_two(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)


total = sum_of_two(10, 5)
print(total)

# Tesla exercise
# def checkDriverAge(age=0):
#         # age = input("What is your age?: ")
#         if int(age) < 18:
# 	        print("Sorry, you are too young to drive this car. Powering off")
#         elif int(age) > 18:
# 	        print("Powering On. Enjoy the ride!")
#         elif int(age) == 18:
#             print("Congratulations on your first year of driving. Enjoy the ride!")

# checkDriverAge(18)


# Methods vs Functions
# methods are always owned by something unlike functions, in this case it is the string 'hello'.
print('hello'.capitalize())


# Docstrings
def test(a):
    '''
    Info: this function tests and prints so and so parameters'''
    print(a)


# help(test)
print(test.__doc__)


# Clean code
def is_even(num):
    if num % 2 == 0:
        return True
    # elif num % 2 != 0:
    return False


print(is_even(52))
# cleaner way


def is_even(num):
    return num % 2 == 0  # this is efficient thinking


print(is_even(51))
