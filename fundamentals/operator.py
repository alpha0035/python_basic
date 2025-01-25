# Arithmetic operator
a = 34
b = 3
print("Add: ", a+b)
print("Sub: ", a-b)
print("Division: ", a/b)
print("Floor division: ", a//b)
print("Module: ", a%b)
print("Multiply: ", a*b)
print("Exponent: ", a**b)

# Comparison operator
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

# Logical operator
a= True
b= False
print(a and b)
print(a or b)
print(not a)

# Identity operator
# to check if two values are located on the same part of the memory
# Note: Two variables that are equal do not imply that they are identical. 
x= 20
y= 20
z= x
print(x is y)
print(x is not y)
print(x is z)

# Membership operator
# to test whether a value or variable is in a sequence.
x = 20
y = 55
l = [20, 33, 64, 50]
print(x in l)
print(x not in l)
print(y in l)

# Terary operator
# known as conditional expressions, are operators that evaluate something based on a condition being true or false
# sytax: [on_true] if [expression] else [on_false]
x = 10
y = 20
min = x if x<y else y
print(min)