# Generators

range(100)
list(range(100))

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = make_list(100)
print(my_list)

def generator_function(num):
    for i in range(num):
        yield i*2           # yield keyword pauses the function.
        
g = generator_function(100)
print(g)
next(g)
next(g)
next(g)
print(next(g)) 
        
# for item in generator_function(100):
#     print(item)

# Generators Performance
from time import time
def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(100000):
        i*5
@performance
def long_time2():
    print('2')
    for i in list(range(100000)):
        i*5


long_time()
long_time2()

# Under the hood generators
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator)*2)
        except StopIteration:
            break
        
special_for([1,2,3])


class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    def __iter__(self):
        return self 
    
    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration
    
gen = MyGen(0,100)
for i in gen:
    print(i)
    
# Fibonacci Numbers

def fib(num):
    nums = []
    num1 = 0
    num2 = 1 
    for i in range(num):
        nums.append(num1)
        temp = num1
        num1 = num2
        num2 = temp + num2
    return nums

series = fib(20)
print(series, 'series')

def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b 
        b = temp + b
        
for x in fib(20):
    print(x)
    
