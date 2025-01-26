# special statements that help control the execution of loops

# break statement
# used to exit a loop. The program immediately exits the loop, and the control moves to the next line of code after the loop.
for i in range(5):
    if i==4: 
        break
    print("i is less than 4", i)

# continue statement 
# skipping the rest of the code inside the loop for the current iteration only and the next iteration of the loop will begin
for i in range(5):
    if i<=3:
        continue
    print('i is greater than 3', i)

# pass statement
# a null operation or a placeholder. It does nothing but allows us to maintain the structure of our program.
for i in range(5):
    if i<4:
        pass
    print(i)