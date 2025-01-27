# use to define function
# def function_name: 
#     function definition statements…
# In the case of classes, the def keyword is used for defining the methods of a class.
# def keyword is also required to define the special member function of a class like __init__()

def funct():
    print("Hello function")
funct()

def sub(x, y):
    return x-y
print(sub(4, 10))

# Passing function as arg
# We can pass a function by simply referencing its name without parentheses.
def func1(func2, arg):
    return func2(arg)
def add(arg):
    return arg+1
def sub(arg):
    return arg-1
def square(arg):
    return arg**2

x= int(input("Enter a number: "))
print(func1(add, x))
print(func1(sub, x))
print(func1(square, x))

# With *args
# *args is used to pass a variable number of arguments to a function
# * allows a function to accept any number of positional arguments.
# This is useful when we are not sure how many arguments will be passed to the function.
def sum(*arg):
    c = 0 
    for i in arg:
        c+=i
    return c
print(sum(1, 2, 3, 5))
print(sum(2, 5, 7, 8, 10))

# With **kwargs
# used to pass a variable number of keyword arguments to a function
# This allows the function to accept any number of named (keyword) arguments.
def printInfo(**arg):
    for key, val in arg.items():
        print(f"{key} : {val}")
printInfo(name = 'alpha', size = 100, rate = 5.3)

# Note: def also use to define methods in class
class Alpha:
    def greet():
        print('Greeting from Alpha!')