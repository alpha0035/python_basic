# It is a data structure that allows adding and removing elements from both ends efficiently
# a deque supports both FIFO and LIFO operations
from collections import deque

# types of restricted dqueue
# Input Restricted Deque:  Input is limited at one end while deletion is permitted at both ends.
# Output Restricted Deque: output is limited at one end but insertion is permitted at both ends.

# Operations on dqueue
# Appending and deleting
# append(x): Adds x to the right end of the deque.
# appendleft(x): Adds x to the left end of the deque.
# extend(iterable): Adds all elements from the iterable to the right end.
# extendleft(iterable): Adds all elements from the iterable to the left end (in reverse order).
# remove(value): Removes the first occurrence of the specified value from the deque. If value is not found, it raises a ValueError.
# pop(): Removes and returns an element from the right end.
# popleft(): Removes and returns an element from the left end.
# clear(): Removes all elements from the deque.
dq = deque([10, 20, 30])

# Add elements to the right
dq.append(40)  

# Add elements to the left
dq.appendleft(5)  

# extend(iterable)
dq.extend([50, 60, 70]) 
print("After extend([50, 60, 70]):", dq)

# extendleft(iterable)
dq.extendleft([0, 5])  
print("After extendleft([0, 5]):", dq)

# remove method
dq.remove(20)
print("After remove(20):", dq)

# Remove elements from the right
dq.pop()

# Remove elements from the left
dq.popleft()  

print("After pop and popleft:", dq)

# clear() - Removes all elements from the deque
dq.clear()  # deque: []
print("After clear():", dq)

# Accessing items
# Indexing: Access elements by position using positive or negative indices.
# len(): Returns the number of elements in the deque.
dq = deque([1, 2, 3, 3, 4, 2, 4])

# Accessing elements by index
print(dq[0])  
print(dq[-1]) 

# Finding the length of the deque
print(len(dq))

# Count, Rotation and Reversal
# count(value): This method counts the number of occurrences of a specific element in the deque.
# rotate(n): This method rotates the deque by n steps. Positive n rotates to the right and negative n rotates to the left.
# reverse(): This method reverses the order of elements in the deque.
dq = deque([10, 20, 30, 40, 50, 20, 30, 20])

# 1. Counting occurrences of a value
print(dq.count(20))  # Occurrences of 20
print(dq.count(30))  # Occurrences of 30

# 2. Rotating the deque
dq.rotate(2)  # Rotate the deque 2 steps to the right
print(dq)

dq.rotate(-3)  # Rotate the deque 3 steps to the left
print(dq)

# 3. Reversing the deque
dq.reverse()  # Reverse the deque
print(dq)