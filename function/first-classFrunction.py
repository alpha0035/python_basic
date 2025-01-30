# is a concept where functions are treated as first-class citizens
# treat like any other variable

# Assigning functions to variable
# We can assign function to a variable then use variable to call function
def f1():
    print("Hello func1!")
var = f1
var()

# Passing fuction as argument
# we can pass function as arg of other fuctions
def f2(x):
    x()
    pass
f2(var)

# Returning function
def f3(x):
    return x**2
def f4(x):
    return f3(x)

# Storing function in data structures
# function can be stored in data structures like list or dictionary
def f5(x, y):
    return x*y
def f6(x, y):
    return x/y
list = [f5, f6]
for i in list:
    print(i(3, 2))
dict = {'one': f5, 'two': f6}
for i in dict.values():
    print(i(3, 2))