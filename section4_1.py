# *args **kwargs
def super_func(*args, **kwargs):
    total = 0
    print(kwargs)
    for items in kwargs.values():
        total += items
    return sum(args) + total

<<<<<<< HEAD

print(super_func(1, 2, 3, 4, 5, num1=5, num2=6))

# Rule: params, *args, default parameters, **kwargs


# Exercise: Find the highest even
def highest_even(num):
    h_even = 0
    even = 0
    for i in range(0, len(num)):
        if num[i] % 2 == 0:
            even = num[i]
            if even > h_even:
                h_even = even
    return h_even


print('Highest even from list:', highest_even([1, 2, 4, 6, 7, 9, 12, 13, 14]))

# solution


def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11]))


# Walrus Operator := assigns values to variables as part of a larger expression.
a = 'hellooooooo'

if ((n := len(a)) > 10):
    print(f'too long {n} elements')

while((n := len(a)) > 1):
    print(n)
    a = a[:-1]

print(a)

# Scope- what variables do I have access to? which means who has access to whom.
a = 1


def parent():
    a = 10

    def confusion():
        #a = 50
        return a
    return confusion()


print(a)
print(parent())
print(a)

# 1. start with local
# 2. parent local?
# 3. Global
# 4. built in python functions. One can return built in functions like sum.


# Global keyword
a = 10


def confusion(b):  # parameters are local variables of the function
    print(b)
    a = 90


confusion(300)

total = 0


def count():
    global total
    total += 1
    return total


count()
count()
print(count())


def count(total):
    total += 1
    return total


print(count(count(count(total))))  # without having to use global keyword

# Non local keyword


def outer():
    x = 'local'

    def inner():
        nonlocal x  # run by commenting this line and see the difference for yourself about keyword nonlocal
        x = 'nonlocal'
        print('inner:', x)

    inner()
    print('outer:', x)


outer()

print(help())
=======
print(super_func(1,2,3,4,5))

>>>>>>> dffc9a63eefc12287fcef593cbf0fc139d2f9d41
