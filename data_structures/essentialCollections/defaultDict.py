# It is a sub-class of the dictionary class that returns a dictionary-like object.
# The difference from dictionary is, It provides a default value for the key that does not exist and never raises a KeyError.
from collections import defaultdict

# Syntax: defaultdict(default_factory)
# Parameters:  
# default_factory: A function returning the default value for the dictionary defined. If this argument is absent then the dictionary raises a KeyError.


# Common Use Cases for defaultdict
print("""1.Using List as Default factory
2.Using int as Default factory
3.Using str as Default factory""")
def gen():
    for i in range(0, 20):
        print('*', end='')
    print()
choice = int(input("Enter your choice: "))
gen()
match choice:
    case 1:
        # Using List as Default Factory
        # Defining a dict
        d = defaultdict(list)

        for i in range(5):
            d[i].append(i)

        print("Dictionary with values as list:")
        print(d)
    case 2:
        # Using int Default Factory
        # Defining the dict
        d = defaultdict(int)

        L = [1, 2, 3, 4, 2, 4, 1, 2]

        # Iterate through the list
        # for keeping the count
        for i in L:

            # The default value is 0
            # so there is no need to 
            # enter the key first
            d[i] += 1

        print(d)
    case 3:
        # Using str Default Factory
        # Using str as the factory function
        str_defaultdict = defaultdict(str)
        str_defaultdict['greeting'] = 'Hello'
        print(str_defaultdict)
gen()

