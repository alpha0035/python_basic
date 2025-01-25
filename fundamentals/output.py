#printing output
print("Print output in python")
print("Hello", "This is printing")

# print single or multiply output
s = "Hi"
print(s)
a = 25
print(s,a)

# To format output, we use format() 
range = 33.33333
print("Range: {0:.2f}".format(range))
print("String: {0}, a: {1}".format(s, a))
# using sep and end parameter
# the end will print character at the end
print("I'm Alpha", end="07")
print("@")
# the sep is used to specify the separator between the values that are passed
print("24","01","2025", sep='-')
#using f-string
name= "Alpha"
team= 7
print(f"Hello from {name} of {team}")
#using % operator
print("The name is %s" %name)