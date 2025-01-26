# A tuple is an immutable ordered collection of elments
# Tuple can hold elements of different datatypes

# Creating a tuple
a = (1, "alpha", 0.5)
b = [2, "beta", 0.3]
b = tuple(b)
c = tuple((3, "gamma", 0.9))
print(a)
print(b)
print(c)

# Operations

# accessing of tuple: we can access element of tuple by using indexing and slicing
# using indexing
print(a[2])
# accessing range of elements using slicing
print(b[1:3])
print(b[:2])

# concatenation of tuple: using + operator. This will create new tuple
# Note: only same datatypes can be concatenate, an error will arise if a list + a tuple
combine = a + b
print(combine)

# slicing of tuple
# syntax: tuple[start:stop:step]
# print from second element
print(combine[1:])
# reverse the tuple
print(combine[::-1])
# print element from range
print(combine[2:5])

# deleting tuple
del combine

