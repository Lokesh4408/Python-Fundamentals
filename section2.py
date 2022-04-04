#name = input('what is your name?')
#print('Yelloooo ' + name)

#Fundamental Data types
from soupsieve import comments


int 
float
bool
str
list
tuple
set
dict
# complex

print(2 ** 3)
print(5 // 4)
print(6 % 4)
#Classes --> custom types

#Specialized Data Types: like Modules

#None: means nothing, absence of value

#operator precedence
# ()
# **
# * /
# + -
print((5 + 4) * 10 / 2) # float 45
print(((5 + 4) * 10) / 2) # float 45 
print((5 + 4) * (10 / 2)) # float 45
print(5 + (4 * 10) / 2) # float 25
print(5 + 4 * 10 // 2) # integer 25

print(bin(5))
print(int('0b1011', 2)) #base 2

user_iq = 190 #variable
print(user_iq)

#Expressions vs STatements
iq = 100
user_age = iq / 5
print(user_age)

#augmented assignment operator
some_value = 5
some_value += 2
some_value -= 1
print(some_value)

#strings
print(type("hi hello there"))
user_name = 'supercoder'
password = 'supersecret'
long_string = '''
Wow
0 o
---
'''
print(long_string)
first_name = 'lokesh'
last_name = 'munagala'
full_name = first_name + ' ' + last_name
print(full_name)

#string concatenation
print('hello' + ' 5')

#type conversion
input = [9,8,7,6,5,4,3,2,1,0]
targetlist = {}
resultlist = {}
def targeted(input):
        k = 0
        for i in range(10):
            for j in range(10):
                result = input[i] + input[j]
                target = [i,j]
                if k < 10:
                    targetlist[k] = target
                    resultlist[k] = result
                    k+=1
        return targetlist,resultlist

output, sum = targeted(input)
#print(f'sum of values: {sum}, target indices: {output}')

#type conversion
a = str(100)
b = int(a)
c = type(b)
print(c)
print(type(int(str(100))))

# Escape Sequence
weather = '\t It\'s sunny \n hope you have a good day'
print(weather)

# formatted strings
name = 'Johnny'
age = 54
print('hi ' + name + '. You are ' + str(age) + ' years old.')
print(f'hi {name}. You are {age} years old.')

# String indices, [start:stop:stepover]
selfish = 'me me me'
print(selfish[::-1]) #reverse of the string

# Immutability: single element in a string cannot be changed with assignment, entire string should be changed.

# Builtin functions
print(len('hellllloooo'))
greet = 'helloooo'
print(greet[0:len(greet)])
quote = 'to be or not to be'
print(quote.replace('be', 'me'))
print(quote)

# Booleans
name = 'Lokesh'
is_cool = False
is_cool = True
print(is_cool)

# Exercise: type conversion
name = 'Lokesh Reddy'
age = 50
relationship_status = 'single' # this assigns a string to the variable

relationship_status = 'it\'s complicated'
print(relationship_status)

print(" \n which year were you born? ")
#birthY = input("year of birth: ")
#print(type(birthY))
#age = 2022 - birth_y
#print(f'your age is: {age}')

# Commenting your code

'''using control + backward slash  (shift + 7)
line 1 comment 
line 2 comment
line3 comment
unlimited number of comments
just keeps going on and on
like this
without meaning and more lines'''

# Password checker
# username = input('whats your username? ')
# password = input('whats your password? ')

password_length = len(password)
hidden_password = '*' * password_length

#print(f'{username}, password {password} is {password_length} letters long')
print('*' * 10)

# Lists in python
li = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1,2,'a', True]
amazon_cart = ['notebooks', 
               'sunglasses',
               'toys',
               'grapes'
               ]
amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:] # try assigning amazon cart without square brackets
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

# Data Structure: List slicing (lists are mutable)
# Matrix

