# If the return statement is without any expression, then the special value None is returned.
# def function_name(parameters):
#     # Function body
#     return value

# return multiple value
def func():
    name = 'alpha'
    rate = 5.3
    return name, rate
x, y = func()
print(f"{x} : {y}")

# return list
def rangeX(n):
    return [n**2, n**3]
list = rangeX(4)
print(list)

# return another function
def func2(n):
    return rangeX(n)
list = func2(4)
print(list)