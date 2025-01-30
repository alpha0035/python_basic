# create a class
class Alpha:
    name = 'alpha'

# create objects
alp1 = Alpha()
print(alp1.name)

# using __init__() function
class Beta:
    type = 2
    def __init__(self, name, size):
        self.name = name
        self.size = size
bta1 = Beta('beta', 0.45)
print(bta1.name, bta1.size)

# self parameter
# is a reference to the current instance of the class. It allows us to access the attributes and methods of the object

# __str__ method
# allows us to define a custom string representation of an object
class Gamma:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    def __str__(self):
        return f"<class_Gamma> {self.name} - {self.size}"
gma = Gamma('ymm', 0.35)
print(gma.__str__())