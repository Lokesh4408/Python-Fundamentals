#name = input('what is your name?')
#print('Yelloooo ' + name)

#Fundamental Data types
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

# 


