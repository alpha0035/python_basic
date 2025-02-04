# list is a built-in dynamic sized array (automatically grows and shrinks)
# A list may contain mixed type of items
# List can contain duplicate items.
# List in Python are Mutable. Hence, we can modify, replace or delete the items.
# List are ordered. It maintain the order of elements based on how they are added.
# Accessing items in List can be done directly using their position (index), starting from 0.
a = [1, "string", 5.9] # list example

# Creating a list
a = [1, 2, 3]
b = list((1, 2, 3))
c = [4]*3
print(a)
print(b)
print(c)

# Accessing list elment
print(a[0])
print(b[-1])

# Adding elment
a.append(4) # adds an elment at the end of list
b.extend([4, 5, 6]) # adds multiply elments at the end of list
c.insert(0, 3) # adds an elment at specify position
print(a)
print(b)
print(c)

# Updating elment
c[2]= 5
c[3]= 6
print(c)

# Removing elment
a.remove(3) # remove the first occurence of an elment
b.pop() # remove an elment at specific index or at the end of list if no 
del c[0] # delete an elment at specified index

# Iterating over list
a = [30, "alpha", 1.553]
for i in a:
    print(i)
    print(type(i))

# Nested list
a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in a:
    for j in i:
        print(j, end=" ")
    print()