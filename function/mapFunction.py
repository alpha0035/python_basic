#  is used to apply a given function to every item of an iterable, such as a list or tuple, and returns a map object (which is an iterator)
# Syntax: map(function, iterable)
# function: The function we want to apply to every element of the iterable.
# iterable: The iterable whose elements we want to process.

# Converting map object to a list
# By default, the map() function returns a map object, which is an iterator. 
# In many cases, we will need to convert this iterator to a list to work with the results directly.
a = [1, 2, 3]
def f1(val):
    return val**2
res = map(f1, a)
print(type(res))
x = list(res)
print(type(x))
print(x)

# map with lambda
# We can use a lambda function instead of a custom function
res = map(lambda val: val*2+1, a)
print(list(res))

# map with multiply iterables

odd = [1, 3, 5, 7]
even = [2, 4, 6, 8]
res = map(lambda x,y: x*y, odd, even)
print(list(res))