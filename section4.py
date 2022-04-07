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
