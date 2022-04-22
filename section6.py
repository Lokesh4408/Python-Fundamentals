# OOP
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
cat2 = Cat('Bobby', 2)
cat3 = Cat('Brown', 3)

# 2 Create a function that finds the oldest cat

print(cat1.age)
