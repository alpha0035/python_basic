# Exception handling in Python is done using the try, except, else and finally blocks.
# Syntax:
# try:
#       # Code that might raise an exception
# except SomeException:
#       # Code to handle the exception
# else:
#      # Code to run if no exception occurs
# finally:
#     # Code to run regardless of whether an exception occurs

print("""1.Catching exceptions
2.Raise an Exception""")
choice = int(input("Enter your choice "))
def gen():
    for i in range(0, 20):
        print('*', end='')
    print()
gen()

match choice:
    case 1:
        # Python Catching Exceptions
        print("""1.Catching specific exceptions
2.Catching multiply exceptions
3.Catch-All Handlers""")
        choice2 = int(input("Enter your choice: "))
        gen()
        match choice2:
            case 1:
                # Catching Specific Exceptions
                try:
                    x = int(input())
                    y = 1/x
                except ValueError:
                    print('Not valid input!')
                except ZeroDivisionError:
                    print('Divide Zero')
            case 2:
                # Catching Multiple Exceptions
                li = ['alpha', 1, 0.33]
                try:
                    total = int(li[0])+ int(li[1])
                except (ValueError, TypeError) as e:
                    print(e)
            case 3:
                # Catch-All Handlers
                try:
                    x = int(input("Enter an integer: "))
                except:
                    print("Something went wrong!")
    case 2:
        gen()
        # Raise an Exception
        # using the 'raise' keyword followed by an instance of the exception class that we want to trigger
        # We can choose from built-in exceptions or define our own custom exceptions by inheriting from Python’s built-in Exception class
        # Syntax: raise ExceptionType(“Error message”)
        def setAge(age):
            if age<0:
                raise ValueError("Age cann't be negative")
            print(f"Age is set to {age}")
        try:
            setAge(int(input("Enter your age: ")))
        except ValueError as e:
            print(e)