# Part A
# 1. Create a list of ‘ages’ with the following values: 5 , 6, 24, 32, 21, 70
ages = [5, 6, 24, 32, 21, 70]

# 2. The condition of the while loop should look for ages under 30

# 3. Each cycle in the while loop, should get a value out of the list
# (Hint : Use a counter)
counter = 0
while ages[counter] < 30:

# 4. Print each tested cell inside the loop
    print('the age is : ' +str(ages[counter]))
    counter += 1

# 5. Once the condition is false, print the cell that caused it
print('value that caused loop to stop : ' +str(ages[counter]))

# 6. Add empty new line between Part A and Part B
print('\n')

# Part B
# 1. Use the same list from Part A

# 2. Create a new while loop, with the same ‘stop’ condition as in Part A
counter = 0
while ages[counter] < 30:

# 3. Also, if the age is bigger then 20 - stop the ‘while’ loop from inside.
# Right before the stop of the loop, print the tested value out of the list
    if ages[counter] > 20:
        print('value that stopped loop : ' +str(ages[counter]))
        break

    counter += 1

print('\n')

# Part C
# 1. Create a while loop, based on the list from Part A.
# Loop’s condition should check whether the age is smaller than 70
counter = 0
while ages[counter] < 70:

# 2. On each cycle of the loop, change list’s cell to be ‘+2’ and print it
    ages[counter] = ages[counter] + 2
    print("cell's new value is : " +str(ages[counter]))

    counter += 1

# 3. If the loop reaches to the number 70, it should run an ‘else’ part with the print :
# “I’m inside ‘else’ because of *listCell*’
else:
    print("I'm inside 'else' because of the number : " +str(ages[counter]))