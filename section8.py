# Decorators
def hello():
    print('hellllloooo')


greet = hello
del hello

print(greet())


def hello(func):
    func()


def greet():
    print('still here!')


a = hello(greet)
print(a)

# Higher Order Function HOF


def greet(func):
    func()


def greet2():
    def func():
        return 5
    return func

# Higher order functions are those which accepts functions as parameters or returns functions as an end result.


# Decorator

def my_decorator(func):
    def wrap_func():
        print('**********')
        func()
        print('**********')
    return wrap_func


@my_decorator
def hello():
    print('hellllooooo')


@my_decorator
def bye():
    print('see ya later')


# my_decorator(hello)() - this should also do the same job as a decorator.
hello()
bye()


def my_decorator1(func):
    def wrap_func(x):
        print('***********')
        func(x)
        print('***********')
    return wrap_func


@my_decorator1
def hello(greeting):
    print(greeting)


hello('hallo')
