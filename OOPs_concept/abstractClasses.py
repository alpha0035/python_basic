# is a class that cannot be instantiated on its own and is designed to be a blueprint for other classes

# abstract base class in python
# defines methods that must be implemented by its subclasses, ensuring that the subclasses follow a consistent structure
# ABCs allow you to define common interfaces that various subclasses can implement while enforcing a level of abstraction.
# Python provides the abc module to define ABCs and enforce the implementation of abstract methods in subclasses.
from abc import ABC, abstractmethod
# define an abstract class
class Alpha(ABC):
    @abstractmethod
    def func1(self):
        pass

# concreate subclass 
class Beta(Alpha):
    def func1(self):
        return "Hello"

bta = Beta()
print(bta.func1())

# abstract method
class Gamma(ABC):
    @abstractmethod
    def greet(self):
        pass
    def bye(self):
        pass

# concrete method
class Delta(ABC):
    @abstractmethod
    def greet(self):
        pass

    def bye(self):
        return "Say bye! From delta!"
class Zeta(Delta):
    def greet(self):
        return "Say hello! From zeta!"
zta = Zeta()
print(zta.bye())

# abstract poperities
# like abstract methods but are used for properties
class Eta(ABC):
    @property
    @abstractmethod
    def greet(self):
        pass # Abstract property, must be implemented by subclasses
class Iota(Eta):
    @property
    def greet(self):
        return "Say hello! From iota!"
ita = Iota()
print(ita.greet)

# abstract class instantiation
# Abstract classes cannot be instantiated directly. 
# This is because they contain one or more abstract methods or properties that lack implementations. 
# Attempting to instantiate an abstract class results in a TypeError.