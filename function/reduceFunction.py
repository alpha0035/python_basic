# is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along
# This function is defined in “functools” module.
from functools import reduce
# Syntax: reduce(function, iterable[, initializer])
# function: A function that takes two arguments and performs an operation on them.
# iterable: An iterable whose elements are processed by the function.
# initializer (optional): A starting value for the operation. If provided, it is placed before the first element in the iterable.

# reduce with lambda
a = [2, 3, 4, 5]
res = reduce(lambda x, y: x+y, a)
print(res)

# reduce with operator function 
import operator
res = reduce(operator.add, a)
print(res)
res = reduce(operator.mul, a)
print(res)