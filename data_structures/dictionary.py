# store value in key:value pair
# key can't be repeated and must be immutable
# value can be duplicated and of any datatype
d = {1:9, 2:'hello'} # dictionary example
print(d)
print(type(d))

# Create a dictionary
# using {}
a = {1: 'alpha', 2: 'beta', 3: 'gamma'}
# using dict()
b = dict(one = 'alpha',two = 'beta', three = 'gamma')
print(a)
print(b)

# Accessing 
print(a[1])
print(b['two'])

# Removing
# using del remove an item by key
del a[3]
print(a)
# using pop() remove an item by key and return its value
print(b.pop('three'))
print(b)
# popitem() remove and return the last key-value pair
print(a.popitem())
print(a)
# clear() empty dictionary
a.clear()
print(a)

# Iterating
# key: using keys() with for loop
# value: using values() with for loop
# both: using items() with for loop
a = {1: 'alpha', 2: 'beta', 3: 'gamma'}
for i in a.keys():
    print(i)
for i in a.values():
    print(i)
for i in a.items():
    print(i)

# Nested dictionary
a = {1: 'alpha', 2: 'beta', 
     3: {'one': 1, 'two': 2}}
print(a)