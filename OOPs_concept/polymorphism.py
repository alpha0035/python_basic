# in built-in functions
print(len([1, 2, 3])) #length of list
print(len('alpha')) #length of string

# in functions
# Duck typing enables functions to work with any object regardless of its type.
def add(x, y):
    return x + y
print(add(3, 4))
print(add('alpha', 'seven'))
print(add([0, 2, 4], [1, 3, 5]))

# in operators
# In Python, operators like + behave polymorphically, performing addition, concatenation or merging based on the data type.
print(5 + 10)  # Integer addition
print("Hello " + "World!")  # String concatenation
print([1, 2] + [3, 4])  # List concatenation

# in oops
# polymorphism allows methods in different classes to share the same name but perform distinct tasks. 
# This is achieved through inheritance and interface design.
class Alpha:
    def countingRate(self):
        return 'undefine'
class Beta(Alpha):
    def __init__(self, type, size):
        self.type = type
        self.size = size
    def countingRate(self):
        return self.type**self.size
class Gamma(Alpha):
    def __init__(self, rate):
        self.rate = rate
    def countingRate(self):
        return self.rate**self.rate
alps = [Beta(3.3, 2.9), Gamma(0.8)]
for alp in alps:
    print(f"Counting Rate: {alp.countingRate()}")