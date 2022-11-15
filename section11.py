# Modules in python
# using utils as a functions holder and call them into main.py after importing the module.

# if __name__ = __main__:
#   print("Im inside the main file")

class Student():
    pass

std1 = Student()
print(type(std1)) # this tells that Student class has been created inside the main file. Not from Utils or any other place.

# Built-in Modules

import random

print(random) # built-in module
print(dir(random))
print(random.random()) # it always gives out values between 0 and 1.
print(random.randint(1,14))
print(random.choice([1,2,3,4,5,6]))

my_list = [1,2,3,4,5,6]
random.shuffle(my_list)
print(my_list)

# Built-in Modules 2
import sys

# first = sys.argv[1]
# last = sys.argv[2]
# print(f'Your name is {first} {last}') # one can give inputs directly from the command line.

# num1 = sys.argv[1]
# num2 = sys.argv[2]

# actual = random.randint(1,20)
# guess = input('Guess an integer number from 1 to 20:')

# if guess == actual:
#     print('You are a gpsyy!')
# else:
#     print('guess again!')


# Exercise: Ask the user to guess from a range of integers & to input via terminal. Then praise him/her if they get it right.
from random import randint
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        guess = int(input(f'guess a number {sys.argv[1]} ~ {sys.argv[2]}: '))
        if 0<guess<15:
            if guess == answer:
                print('you might be a genius!')
                break
        else:
            print('hey arschloch, zwischen ein und feunfsehn.')
    except (ValueError, TypeError):
        print('please enter a number to guess again: ')
        continue
    


