#Taking single input
x= input("Value: ")
print(x)

# Taking multiply input
# Using input() and split()
x, y, z = input("Value: ").split()
print(x, y, z, sep='-')
# Using list comprehension
# syntax of list comprehension: [expression for item in iterable if condition]
inputs = [i for i in input().split()]
print(inputs)
# Using map() for multiply integer inputs
a = map(int, input().split())
b = list(a)
print(b)
# Using a loop
# create empty list to store inputs
a = []
b = int(input("How many input? "))
# loop to collect all inputs
for i in range(b):
    val = int(input())
    a.append(val)
for i in a:
    print(i)

# Take conditional input
# the default type is always string, so you need type cast
x = float(input("Enter the percent: "))

# Find data type for input
a= 20
x= "Hello"
y= '_'
z = 45.3
t= input()
print(type(a), type(x), type(y), type(z), type(t))