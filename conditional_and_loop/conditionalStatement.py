# if
age = int(input("Enter age: "))
if age>=18: 
    print("Can pass")

# if ... else
if age>19 and age<24:
    print("Greating!")
else:
    print("Good!")

# elif
if age<18:
    print("Get back")
elif age>=18 and age<20:
    print("Stage A")
elif age==20 or age>25:
    print("Stage B")
else:
    print("Option")

# Nested if ... else
if age<18:
    if age>=15:
        print("Tomorrow")
    elif age<15 and age>=10:
        print("Last moth")
    else:
        print("Last year")
else:
    pass

# match-case
match age:
    case 18: 
        print("Nearly")
    case 19|20: 
        print("Good")
    case _: 
        print("...")