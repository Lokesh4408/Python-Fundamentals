# 4 pillars of OOP: Encapsulation, Abstraction, Inheritance and Polymorphism
# Encapsulation
class PlayerCharacter:
    def __init__(self, name, age): # Dunder method, which is inbuilt in python.
        self._name = name # self.name = name . Here when underscore is used it signifies that it is a private variable and not be changed.
        self._age = age # self.age = age
        
    def speak(self):
        print(f'my name is {self._name}, and I am {self._age} years old.')
        
player1 = PlayerCharacter('lokesh', 25)
print(player1.speak())
# print(player1.name)
# print(player1.age)

# player2 = {'name': 'andrei', 'age': 25}
# print(player2['name'])
# print(player2['age'])

# # Abstraction
# player1.speak()
# print((1,2,3,1).count(1))
# camera.picture()
player1.name = '!!!'
player1.speak = 'Boooo'

print(player1.speak)

# Inheritance
class User:
    def sign_in(self):
        print('logged in')
        
    def attack(self):
        print('do nothing')
        
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power 
        
    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}.')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
        
    def attack(self):
        print(f'attacking with arrows: arrows left {self.num_arrows}.')

wizard1 = Wizard('merlin', 60)
archer1 = Archer('robin', 100)
print(wizard1.sign_in())
wizard1.attack()
archer1.attack()

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))

# Polymorphism
def player_attack(char):
    char.attack()
    
player_attack(wizard1)
player_attack(archer1)
print(wizard1.attack())

for char in [wizard1, archer1]:
    char.attack()