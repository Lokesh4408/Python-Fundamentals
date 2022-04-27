# OOP
import numpy as np


class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name, age):  # this is a constructor function
        if (self.membership):
            self.name = name  # attributes
            self.age = age

    def run(self):
        print('run')
        return 'done'

    def shout(self):
        print(f'my name is {self.name}')
        
    @classmethod
    def addings_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)
    
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

print(PlayerCharacter.addings_things(21,3)) # classmethods can be used before instanciating the classes.
player1 = PlayerCharacter('Lokesh', 25)
player2 = PlayerCharacter('Erik', 24)

print(player1.name)
print(player2.name)
print(player1.age)
print(player2.age)
print(player1.run())
print(player1.membership)
print(player2.membership)
print(player1.shout())
print(player2.shout())

# Cat exercise


class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Billy', 1)
cat2 = Cat('Bobby', 8)
cat3 = Cat('Brown', 6)

# 2 Create a function that finds the oldest cat


def oldest(cat1, cat2, cat3):
    #count = 0
    oldest = []
    oldest.append(cat1.age)
    oldest.append(cat2.age)
    oldest.append(cat3.age)
    return np.max(oldest)


print(cat1.age)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
Eldercat = oldest(cat1, cat2, cat3)
print(f'The eldest cat is {Eldercat} years old.')

# Andrei's solution
peanut = Cat('Peanut', 3)
garfield = Cat('Garfield', 5)
snickers = Cat('Snickers', 1)

def get_oldest_cat(*args):
    return max(args)

print(f'The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old.')

 
