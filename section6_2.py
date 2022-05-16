# Pets everywhere
class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add nother Cat
class Button(Cat):
    
    def sing(self, sounds):
        return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Cat('simon', 1), Cat('sally', 2), Cat('button', 2.5)]
# simon = Cat('simon', 1)
# sally = Cat('sally', 2)
# button = Cat('button', 2.5)

#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance
my_pets.walk()

# super()
class User:
    def __init__(self, email):
        self.email = email
        
    def sign_in(self):
        print('logged in')
        
        
class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email) # User.__init__(self, email). Here super() is used to skip writing 'self' under another method while inheritance.
        self.name = name
        self.power = power 
        
    def attack(self):
        #User.attack(self)
        print(f'attacking with power of {self.power}.')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
        
    def attack(self):
        print(f'attacking with arrows: arrows left {self.num_arrows}.')
        
wizard1 = Wizard('Merlin', 70, 'merlin@gmail.com')
print(wizard1.sign_in())
print(wizard1.email)

# introspection
print(dir(wizard1))