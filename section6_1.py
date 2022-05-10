# 4 pillars of OOP: Encapsulation, Abstraction, Inheritance and Polymorphism
# Encapsulation
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
player1 = PlayerCharacter('lokesh', 25)
print(player1.name)
print(player1.age)

player2 = {'name': 'andrei', 'age': 25}
print(player2['name'])
print(player2['age'])

# Abstraction
