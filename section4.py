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

print(bool('hello')) # Truthy
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
print(4>5)
print(4==(8/2))
print('a'>'b') # here comparison of ASCII values take place
print(not(True)) # using not keyword as a function

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
print(10 == 10.0) # output is true
print([] == [])
print('\n')
print(True is True)
print('1' is '1')
print([] is []) # 2 different lists at different places in memory
print(10 is 10)
print([1,2,3] is [1,2,3])

# For loops
for item in 'Zero to Mastery':
    print(item)
    
for item in {1,2,3,4,5}:
    print(item)
    
for item in (1,2,3,4,5):
    for x in ['a', 'b', 'c']:
        print(item, x)
        
# Iterables- list, dictionary, tuple, set, string
# Iterated: one by one check each item in the collection
user = {
    'name':'Golem',
    'age': 5006,
    'can_swin': False
}

for k,v in user.items():
    #key, value = item
    print(k, v)

for item in user.values():
    print(item)
  
for item in user.keys():
    print(item)  
    
# for item in 50: # this gives a typeError saying int object is not iterable, coz 50 can't be iterated. 
#     print(item)
    
# Tricky counter
my_list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in my_list:
    sum = sum + i
print('Total sum of the list:', sum)

# range()
print(range(100))
for i in range(0 ,10, 2):
    print(i)
    
for i in range(10 ,0, -1):
    print(i)

for _ in range(2):
    print(list(range(10)))
    
# enumerate
for i,char in enumerate('Helloo'):
    print(i, char)
    
for i,char in enumerate([1,2,3,4,5]):
    print(i, char)
    
for i,char in enumerate(list(range(10))):
    print(5, char)
    if char == 5:
        print(f'index of 50 is: {i}')
  
        
# while loops: infinite loops
j = 0
while j < 20:
    print(j)
    j = j + 1
    #break
else:   # else only works without break statement in a while loop
    print(f'done printing till {j}')
    
# while True:
#     response = input('say something: ')
#     if response == 'bye':
#         break


# break, continue, pass
my_list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in my_list:
    sum = sum + i
    continue
    print(i)

while sum < len(my_list) + 55:
    pass
    print(sum)
    break
    #continue
    
for item in my_list:
    # thinking about it, don't bug me for a while
    pass

# our First GUI
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
print(f'{picture[2][2]} \n')

value = [[0] * 7] * 6 # np.array([np.zeros(6,7)])
print('value with zeros:', value)
for i in range(6):
    for k in range(7):
        # value[i][j] = picture[i][j]
        #print(picture[i][k])
        if picture[i][k] == 0:
            #value[i][k] = ' '
            #print(picture[i][k])
            print(' ', end='')
            #print(value[i][k])
        elif picture[i][k] == 1:
            #value[i][k] = '*'
            #print(picture[i][k])
            print('*', end='')
            #print(value[i][k])
    print('')
        
#print('value without zeros: ', value)

#1 iterate over picture: solution
for row in picture:
    for pixel in row:
        if (pixel == 1):
            print('*', end='')
        else:
            print(' ', end='')
    print('')
#2 if 0: print ' '
#3 if 1: print *
