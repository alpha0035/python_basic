# In python, variables don't require explicit declaration of type
# The type of variables is inferred base on value assigned

# Assigning value to variable
x= 5
x= "Hola"
# Multiply assignments
a= b = c = 100
a, b, c = 100, 200, "Hola"
# Casting a variable
s = "5"
x = int(s)  #cast to integer
d= 35
c= float(d) #cast to float
f= 24
v= str(f)   #cast to string
print(x, c, v)
# Getting type of variable
# using type()
list = [4, 3, 4]
dict = {3:4, 4:3}
print(type(x))
print(type(c))
print(type(v))
print(type(list))
print(type(dict))
# Delete variable
del s, x, d, c, f, v
# print(v) -> error