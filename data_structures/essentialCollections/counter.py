# Counters are a subclass of the dict class in Python collections module
from collections import Counter
# counter is used to count the occurences of elements in iterable or count the frequency of an item in mapping
# Syntax: class collections.Counter([iterable-or-mapping])

# Creating a Counter
# Creating a Counter from a list
ctr1 = Counter([1, 2, 2, 3, 3, 3])
# Creating a Counter from a dictionary
ctr2 = Counter({1: 2, 2: 3, 3: 1})
# Creating a Counter from a string
ctr3 = Counter('hello')
print(type(ctr1))
print(ctr1)
print(ctr2)
print(ctr3)

# Accessing Counter member
# We can access the count of each element using the element as the key. 
# If an element is not in the Counter, it returns 0.
ctr = Counter([1, 2, 2, 3, 3, 3])

# Accessing count of an element
print(ctr[1])  
print(ctr[2])  
print(ctr[3])  
print(ctr[4])  # (element not present)

# Updating Counter
ctr = Counter([1, 2, 2])
print(ctr)
# Adding new elements
ctr.update([2, 3, 3, 3])
print(ctr)

# Methods
# elements(): Returns an iterator over elements repeating each as many times as its count. Elements are returned in arbitrary order.
ctr = Counter([1, 2, 2, 3, 3, 2])
items = list(ctr.elements())
print(items)
# most_common(): Returns a list of the n most common elements and their counts from the most common to the least. 
# If n is not specified, it returns all elements in the Counter.
ctr = Counter([1, 2, 2, 3, 3, 3])
common = ctr.most_common(2)
print(common)
# subtract(): Subtracts element counts from another iterable or mapping. Counts can go negative.
ctr = Counter([1, 2, 2, 3, 3, 3])
ctr.subtract([2, 3, 3])
print(ctr)

# Arithmetic operations on Counter
ctr1 = Counter([1, 2, 3, 3, 4, 4, 4])
ctr2 = Counter([0, 0, 1, 2, 2, 3, 4])
# addition
print('additon:',ctr1 + ctr2)
# subtraction
print('subtraction:', ctr1 - ctr2)
# intersection
print('intersection:', ctr1 & ctr2)
# union
print('union:',ctr1 | ctr2)