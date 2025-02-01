# Syntax:
# class ParentClass:
#     # Parent class code here
#     pass

# class ChildClass(ParentClass):
#     # Child class code here
#     pass

# 1. Parent Class:
# This is the base class from which other classes inherit.
# It contains attributes and methods that the child class can reuse.
# 2. Child Class:
# This is the derived class that inherits from the parent class.
# The syntax for inheritance is class ChildClass(ParentClass).
# The child class automatically gets all attributes and methods of the parent class unless overridden.
class Alpha:
    x = 'alpha'
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
    def __str__(self):
        return f"Hello! This is {self.name}, rating {self.rate}, from {self.x}"

class Beta(Alpha):
    x = 'beta'
    def __init__(self, name, rate):
        super().__init__(name, rate)
        self.name = name
        self.rate = rate
    def __str__(self):
        return f"Hello! This is {self.name}, rating {self.rate}, from {self.x}"

bta = Beta('ymm', 0.66)
print(bta.__str__())

# Creating a child class
# is a class that inherits poperties and methods from its parent class
# child class can also introduce additional attributes and methods, even override the ones inherited from parent class
class Gamma(Alpha):
    x = 'gamma'
    def __init__(self, name, rate):
        super().__init__(name, rate)

    # overriding
    def __str__(self):
        return f"Hmm! Too deep, {self.name}!"
    # additional attributes and methods
    y = 'Gen 2'
    def new_gen(self, str):
        return str+' '+self.y
gma = Gamma('sese', 0.45)
print(gma.__str__())
print(gma.new_gen('at'))

# __init__() Function
# a constructor method of python
# If the child class does not define its own __init__() method, it will automatically "inherit the one from the parent class".
class Delta(Alpha):
    x = 'delta'
    def __init__(self, name, rate, count):
        super().__init__(name, rate)
        self.count = count

class Epsilon(Alpha):
    x = 'epsilon'
    def __str__(self):
        return f"Oops! Be careful, {self.name} {self.x}"

dta = Delta('D', 0.25, 1)
print(dta.__str__())
esl = Epsilon('iron', 0.58)
print(esl.__str__())

# super() Function
# is used to call parent methods
class Zeta(Alpha):
    x = 'zeta'
    def __str__(self):
        return super().__str__() + f" <Gen_2> {self.name}"
zta = Zeta('Xiaohu', 0.44)
print(zta.__str__())

# Types of inheritance
# 1. Single Inheritance: A child class inherits from one parent class.
# 2. Multiple Inheritance: A child class inherits from more than one parent class.
# 3. Multilevel Inheritance: A class is derived from a class which is also derived from another class.
# 4. Hierarchical Inheritance: Multiple classes inherit from a single parent class.
# 5. Hybrid Inheritance: A combination of more than one type of inheritance.
# Single inheritance
class Eta(Alpha):
    x = 'eta'
print(Eta('lanshe', 0.13).__str__())
# Multiple inheritance
class Theta(Beta, Gamma):
    x = 'theta'
tta = Theta('ppx', 0.54)
print(tta.__str__())
# Multiplevel inheritance
class Iota(Delta):
    x = 'iota'
    def __str__(self):
        return f"Hello! <Gen_3> {self.name} {self.x}"
print(Iota('missing', 0.55, 2).__str__())