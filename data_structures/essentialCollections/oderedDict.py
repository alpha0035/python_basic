# is a dictionary subclass that remembers the order in which keys were first inserted.
# The only difference between dict() and OrderedDict() lies in their handling of key order in Python.
from collections import OrderedDict
print("""1.Key value Change
2.Equality Comparison
3.OrderedDict Reversal
4.Key Insertion at Arbitrary Position
5.Deletion and Re-Inserting
6.Collections Module""")

choice = int(input("Enter choice: "))
def gen():
    for i in range(0, 20):
        print('*', end='')
    print()
gen()

match choice:
    case 1:
# Key value Change in Python Dictionary Order
# If the value of a certain key is changed, the position of the key remains unchanged in OrderedDict
        print("Before:\n")
        od = OrderedDict()
        od['a'] = 1
        od['b'] = 2
        od['c'] = 3
        od['d'] = 4
        for key, value in od.items():
            print(key, value)
        print("\nAfter:\n")
        od['c'] = 5
        for key, value in od.items():
            print(key, value)
    case 2:
# Equality Comparison in Python Dictionary Order
# OrderedDicts in Python can be compared for equality not only based on their content but also considering the order of insertion.
        # Create two ordered dictionaries with different orderings
        od1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
        od2 = OrderedDict([('c', 3), ('b', 2), ('a', 1)])

        # Compare the ordered dictionaries for equality
        print(od1 == od2)
    case 3:
# `OrderedDict` does not natively support a `reverse()` method
# the code correctly employs Python’s reversed() function combined with list() and items() to obtain a reversed list of key-value pairs
        my_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

        # Reverse the OrderedDict using reversed()
        reversed_dict = OrderedDict(reversed(list(my_dict.items())))

        # Print the reversed dictionary
        for key, value in reversed_dict.items():
            print(key, value)
    case 4:
# OrderedDict allows inserting a new key at a specific position using the move_to_end method. 
# This flexibility allows dynamic reordering of keys based on usage or priority.
        my_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
        # Move key 'a' to the end
        my_dict.move_to_end('a')
        # Move key 'b' to the beginning
        my_dict.move_to_end('b', last=False)
        for key, value in my_dict.items():
            print(key, value)
    case 5:
        # Deleting and re-inserting the same key will push it to the back as OrderedDict, however, maintains the order of insertion
        print("Before deleting:\n")
        od = OrderedDict()
        od['a'] = 1
        od['b'] = 2
        od['c'] = 3
        od['d'] = 4
        
        for key, value in od.items():
            print(key, value)
        
        print("\nAfter deleting:\n")
        od.pop('c')
        for key, value in od.items():
            print(key, value)
        
        print("\nAfter re-inserting:\n")
        od['c'] = 3
        for key, value in od.items():
            print(key, value)
    case 6:
# Collections Module
# Create an ordered dictionary of key-value pairs
# Set item(key, value): O(1)
# Delete item(key): O(n)
# Iteration: O(n)
# Get item(Key): O(1)
        my_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

        # Add a new item to the end of the dictionary
        my_dict['d'] = 4

        # Add a new item at a specific position in the dictionary
        # my_dict.update({'e': 5, 'f': 6}) or below
        my_dict.update([('e', 5), ('f', 6)])
        my_dict.move_to_end('e', last=False)

        # Iterate over the dictionary in the order in which items were added
        for key, value in my_dict.items():
            print(key, value)

gen()