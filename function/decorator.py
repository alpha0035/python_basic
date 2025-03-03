# A decorator is a function that
#   - Take another function as arg
#   - Return a new function with enhanced functionality
# -> Decorator allow us to add additional functionality to existing function or method in a clean way.
def f1(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@f1 # shorthand for greet = f1(greet)
def greet():
    print("Hello, World!")
greet()

#-------------------------------------#
# Syntax:
# def decorator_name(func):
#     def wrapper(*args, **kwargs):
#         # Add functionality before the original function call
#         result = func(*args, **kwargs)
#         # Add functionality after the original function call
#         return result
#     return wrapper

# @decorator_name
# def function_to_decorate():
#     # Original function code
#     pass

#-------------------------------------#
# 1.decorator_name(func):
# decorator_name: This is the name of the decorator function.
# func: This parameter represents the function being decorated. When you use a decorator, the decorated function is passed to this parameter.
# 2. wrapper(*args, **kwargs):
# wrapper: This is a nested function inside the decorator. It wraps the original function, adding additional functionality.
# *args: This collects any positional arguments passed to the decorated function into a tuple.
# **kwargs: This collects any keyword arguments passed to the decorated function into a dictionary.
# The wrapper function allows the decorator to handle functions with any number and types of arguments.
# 3. @decorator_name:
# This syntax applies the decorator to the function_to_decorate function. It is equivalent to writing function_to_decorate = decorator_name(function_to_decorate).
#-------------------------------------#

# Role in Decorators
# Decorator is type of higher-order function:
    # - Take a function as input
    # - Modify an input function
    # - Return a new function that extends or changes it behaviours.
#-------------------------------------#

# Type of decorators
# 1. Function Decorators
def deco_func(alp):
    def bta_wrapper():
        alp()
    return bta_wrapper
@deco_func
def get():
    print("Hello!")
get()

# 2. Method Decorators
def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Before method execution")
        res = func(self, *args, **kwargs)
        print("After method execution")
        return res
    return wrapper

class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello!")

obj = MyClass()
obj.say_hello()
# 3. Class Decorators
def fun(cls):
    cls.class_name = cls.__name__
    return cls

@fun
class Person:
    pass

print(Person.class_name) 