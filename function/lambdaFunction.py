# anonymous functions means that the function is without a name
# the lambda keyword is used to define an anonymous function in Python
# Syntax: lambda <arguments> : <expression>
# lambda: The keyword to define the function.
# arguments: A comma-separated list of input parameters (like in a regular function).
# expression: A single expression that is evaluated and returned.
s1 = 'alpha'
s2 = lambda f: f.upper()
print(s2(s1))

# Conditional checking
# using if statement
n = lambda x: 'Alpha' if x==1 else 'Beta' if x==2 else 'Gamma'
print(n(1))
print(n(2))
print(n(3))

# Lambda with list comprehension
#  enables us to apply transformations to data in a concise way.
list= [lambda arg=i: arg*10 for i in range(1,10,2) if i>1 and i<9]
for i in list:
    print(i())

# Lambda with multiply statements
# Lambda functions do not allow multiple statements, 
# however, we can create two lambda functions and then call the other lambda function as a parameter to the first function
f = lambda x, y: (x+y, x*y)
print(f(3,4))

# Lambda with filter
n = [1, 1, 3, 4, 1, 2]
list = filter(lambda x: x%2==0, n)
for i in list: print(i)

# Lambda with map
# is called with a lambda function 
# a new list is returned which contains all the lambda-modified items returned by that function for each item.
list = map(lambda x: x*2-1, n)
for i in list:
    print(i)

# Lambda with reduce
# The function is called with a lambda function and an iterable and a new reduced result is returned.
from functools import reduce
b = reduce(lambda x, y: x*y, n)
print(b)