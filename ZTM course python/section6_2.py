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

# 1 Add nother Cat


class Button(Cat):

    def sing(self, sounds):
        return f'{sounds}'


# 2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Cat('simon', 1), Cat('sally', 2), Cat('button', 2.5)]
# simon = Cat('simon', 1)
# sally = Cat('sally', 2)
# button = Cat('button', 2.5)

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

# 4 Output all of the cats walking using the my_pets instance
my_pets.walk()

# super()


class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power): # email
        # User.__init__(self, email). Here super() is used to skip writing 'self' under another method while inheritance.
        # super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        # User.attack(self)
        print(f'attacking with power of {self.power}.')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left {self.num_arrows}.')


# wizard1 = Wizard('Merlin', 70, 'merlin@gmail.com')
# print(wizard1.sign_in())
# print(wizard1.email)

# introspection
# print(dir(wizard1))


# Dunder Methods
class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        return('yess?')

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
# del action_figure
print(action_figure())
print(action_figure['name'])


# SuperList exercise
class SuperList(list):
    def __len__(self):
        return 100
    

super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list)) # is SuperList a subclass of list? 


# Multiple Inheritance

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
        
    def check_arrows(self):
        print(f'{self.arrows} remaining')
        
    def run(self):
        print('run really fast')
        
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self,name, arrows)
        Wizard.__init__(self, name, power)

hb1 = HybridBorg('Serge', 50, 100)
print(hb1.sign_in())

# Method Resolution Order (MRO)
class A:
    num = 10
    
class B(A):
    pass

class C(A):
    num = 1
    
class D(B,C):
    pass 

print(D.mro())

class X: pass
class Y: pass
class Z: pass
class A(X,Y): pass
class B(Y,Z): pass
class M(B,A,Z): pass

print(M.__mro__)


        