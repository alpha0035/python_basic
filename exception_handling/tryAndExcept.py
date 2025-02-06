# In case an error occurs in try-block, Python stops executing try block adn jumps to exception block. 
# These blocks let you handle the errors without crashing the program.
# Syntax:
# try:
#     # Some Code
# except:
#     # Executed if error in the
#     # try block
def gen():
    for i in range(0, 20):
        print('*', end='')
    print()


print("""1.How 'try' work?
2.Else Clause
3.Finally Keyword""")
choice = int(input("Enter your choice: "))
gen()
match choice:
    case 1:
        print("""First, the try clause is executed i.e. the code between try.
If there is no exception, then only the try clause will run, except clause is finished.
If any exception occurs, the try clause will be skipped and except clause will run.
If any exception occurs, but the except clause within the code doesn’t handle it, it is passed on to the outer try statements. If the exception is left unhandled, then the execution stops.
A try statement can have more than one except clause""")
    case 2:
        # you can also use the 'else' clause on the try-except block which must be present after all the except clauses. 
        # The code enters the 'else' block only if the try clause does not raise an exception
        # Program to depict else clause with try-except
 
        # Function which returns a/b
        def AbyB(a , b):
            try:
                c = ((a+b) // (a-b))
            except ZeroDivisionError:
                print ("a/b result in 0")
            else:
                print (c)

        # Driver program to test above function
        AbyB(2.0, 3.0)
        AbyB(3.0, 3.0)
    case 3:
        # a keyword finally, which is always executed after the try and except blocks
        try:
            x, y = input('Enter 2 integer: ').split()
            res = int(x)//int(y)
            print(res)
        except:
            print('Something went wrong!')
        finally:
            print("Program finish!")
