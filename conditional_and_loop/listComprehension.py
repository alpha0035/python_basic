# a way to create a list using concise syntax. This helps us to write cleaner, more readable code compared to traditional looping techniques.
# Syntax: [<expression> for <item> in <iterable> if <condition>]
# expression: The transformation or value to be included in the new list.
# item: The current element taken from the iterable.
# iterable: A sequence or collection (e.g., list, tuple, set).
# condition (optional): A filtering condition that decides whether the current item should be included.

# using comprehension
list = [1, 2, 3, 4, 5]
res = [val*2 for val in list]
print(res)
# it likely to using for loop, but longer:
res = []
for val in list:
    res.append(val*2)
print(res)

# if conditional
res = [val for val in list if val%2==0]
print(res)