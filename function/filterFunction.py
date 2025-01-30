# filters the given iterable with the help of a function that tests each element in the sequence to be true or not.
# Syntax: filter(function, iterable)
# function: A function that defines the condition to filter the elements. This function should return True for items you want to keep and False for those you want to exclude.
# iterable: The iterable you want to filter (e.g., list, tuple, set).

# filter with lambda
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = filter(lambda val: val%2==0, a)
print(type(res))
print(list(res))

# combine filters
b = filter(lambda val: val%2!=0, a)
c= filter(lambda val: val>1 and val<9, b)
print(list(c))