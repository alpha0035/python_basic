# A heap queue or priority queue is a data structure that allows us to quickly access the smallest (min-heap) or largest (max-heap) element
# In Python, heaps are usually implemented as min-heaps

# Creating a Heap Queue
# we first need to import the heapq module
import heapq
# A heap queue is created from a list by calling the heapq.heapify() function, which rearranges the elements of the list into a valid heap structure.
# Creating a list
li = [10, 60, 15, 30, 40]

# Convert the list into a heap
heapq.heapify(li)

print("Heap queue:", li)

# Appending and poping
heapq.heappush(li, 5)
print(li)
x = heapq.heappop(li)
print(li, x, sep='\n')
heapq.heappushpop(li, 30)
print(li)

# Finding largest and smallest elment
# heapq.nlargest(n, iterable) returns the n largest elements from the iterable.
# heapq.nsmallest(n, iterable) returns the n smallest elements from the iterable.
x = heapq.nlargest(3, li)
print(x)
x = heapq.nsmallest(3, li)
print(x)

# Replace and merge
# Creating a heap
h1 = [10, 20, 15, 30, 40]
heapq.heapify(h1)

# Replacing the smallest element (10) with 5
min = heapq.heapreplace(h1, 5)

print(min)
print(h1)

# Merging Heaps
h2 = [2, 4, 6, 8]

# Merging the lists
h3 = list(heapq.merge(h1, h2))
print("Merged heap:", h3)