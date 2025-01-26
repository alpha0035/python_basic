# for var in iterable:
#     # statements
#     pass
# for loops only implement the collection-based iteration

# Loop with string
s = "Alpha"
for i in s:
    print(i)

# Using with range()
# syntax: range(start, stop, step)
for i in range(0, 10, 2):
    print(i, end= ' ')

# pass statement
# The pass statement to write empty loops. Pass is also used for empty control statements, functions, and classes.
for i in s:
    pass
print('do nothing')
# else statement
# Python also allows us to use the else condition for loops. The else block just after for/while is executed only when the loop is NOT terminated by a break statement.
for i in range(1, 5):
    print(i, end=' ')
else: #excute when no break statement
    print('no break')
# enumerate
# is used with the for loop to iterate over an iterable while also keeping track of index of each item.
list = ['alpha', 30, 'high', 0.5]
for i,j in enumerate(list):
    print(i, j)