#python support three types of numbers integer, floating-point, and complex

# Integer, in python, there is no limit to how long an integer value can be.
x = 9
y = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
z = 1_000_000_000
print(z)
print(x+y)
print(type(x+y))

# Float
x= 9.0e3
y= 1.5E2
z= 0.25
print(x, y, z)
print("x / y =", x/y)
print("x // y =", x//y)
print("x % y =", x%y)

# Complex
x= 2 + 3j
y= -2j
print(type(x))
print("abs(x)=", abs(x))
print("real =", x.real)
print("imag =", x.imag)

# Random number
# Generating random Integer
import random
x = random.randint(1, 200)
print(x)
# Generating random floating-point
y = random.uniform(1, 200)
print(y)

# Special number
# NaN : Not a Number
import math
x = math.nan
print(x)
# Infinity
x = float("inf")
y= float("-inf")
print(x)
print(y)