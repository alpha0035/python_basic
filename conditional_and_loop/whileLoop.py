# while expression:
#     statement(s)

count = int(input("Enter a number: "))
while count<5:
    print('getting started')
    count+=1;

# Infinite loop!
# while True:
#     print(count)

# continue and break, pass, else statement
time = 0
while time<9:
    count+=1
    if count==10:
        print('Hello')
    elif count == 14:
        break # exit loop
    elif count == 15:
        continue # continue loop 
    else:
        pass # do nothing
        print('...',time)
    time += 1
else: # excute while no break
    print('no breaking')