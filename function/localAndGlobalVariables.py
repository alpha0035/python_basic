# Local variables
# are initialized in a function and only belong to particular function.
# local variables cann't be accessed outside the function.
def f():
    s = "Local"
    s += 'variable'
    return
f()
# print(s) -> Error

# Global variables
# are defined outside function and can be accessed throughout in program
def f2():
    print("In f2", s)
    return
s = "Variable"
print("Out f2", s)
f2()
# if we try to change gloabal variable value inside function, there will be an error
def test():
    # s+= "..." -> Error
    pass
# global keyword
# this will help to assign or change global variable value
def test2():
    global x
    x+=' !!!'
    pass
x = "Hello"
test2()
print(x)