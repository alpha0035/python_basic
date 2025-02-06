# User-defined exceptions are created by defining a new class that inherits from Python’s built-in Exception class or one of its subclasses
# Define a custom exception class
class AlphaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg
    def __str__(self):
        return f'Alpha exception -> {self.msg}'
# Raise exception
try:
    str = input("Enter your name: ")
    if len(str)==5:
        raise AlphaException("Name mustn't have 5 characters!")
except  AlphaException as e:
    print(e)