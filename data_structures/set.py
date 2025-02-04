# unordered collection of multiple items having different datatypes.
# sets are mutable, unindexed and do not contain duplicates.
# The order of elements in a set is not preserved and can change.

# Creating 
a = {1, 2, 3, 4}
print(a)
# creating set use of list
b = set([1, 2, 3])
# creating set use of tuple
c = set((1, 2, 3))
# creating set use of dictionary
d = set({1: 'a', 2: 'b', 3: 'c'})
print(b)
print(c)
print(d)

# Adding 
# add(): add an elment
a.add(0)
# update(): add multiply elements
a.update([0, 0, 8, 5, 7, 6])
print(a)

# Accessing
for i in a:
    print(i)

# Removing
# remove() method removes a specified element from the set. If the element is not present in the set, it raises a KeyError.
a.remove(0)
print(a)
# discard() method also removes a specified element from the set. Unlike remove(), if the element is not found, it does not raise an error.
a.discard(8)
print(a)
# pop() method removes and returns an arbitrary element from the set. This means we don’t know which element will be removed. If the set is empty, it raises a KeyError.
a.pop()
print(a)