# Python has no character data type so single character is a string of length 1.
# Strings in Python are immutable

# Create a string
x = 'Hello'
y = "Hello"
print(x, y)
x= """Hello
world!"""
y = '''Hello
world!'''
z = """Hello world!"""
print(x, y, z)

# Accessing character
# we can access individual character using indexing
# starting from 0 or -1 from end
s= "Hello world!"
print(s[0], s[3], s[6])
print(s[-1], s[-4], s[-5])

# String slicing
# string[start:end], where start starting index and end is stopping index (excluded)
# Retrieves characters from index 1 to 3: 
print(s[1:4])  
# Retrieves characters from beginning to index 2:
print(s[:3])   
# Retrieves characters from index 3 to the end: 
print(s[3:])   
# Reverse a string
print(s[::-1])

# Common string method
# len(): returns the total number of characters in string
print(len(s))
# uper(): convert all characters to upper case
print(s.upper())
# lower(): convert all characters to lower case
print(s.lower())
# strip(): remove all leading and trailing whitespace in string
print("   Hello    world   !".strip())
# replace(old, new): replaces all occurences of a specify substring with another
print(s.replace("l", "x"))

# Concatenating and repeating 
print(s+s)
print(s*2)