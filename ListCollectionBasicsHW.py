# 1. Create a list of ‘cars’ -
# a. Bwm
# b. Toyota
# c. Tesla
# d. Kia
cars = ['Bmw', 'Toyota', 'Tesla', 'Kia']
print('cars list : ' +str(cars))

# 2. Print out the one before last value of the list
print('second to last value : ' +str(cars[-2]))

# 3. Compare with ‘equals’ sign (using comparison operators) the list’s value in index 1 to the string “Toyota.
# Print out the boolean result
print('car comparison : ' +str(cars[1] == 'Toyota'))

# 4. Create a list of ‘mixed_values’
# a. Jim
# b. 3500
# c. Alex
# d. 2.53
# e. True (without quotation marks))
mixed_values = ['Jim', 3500, 'Alex', 2.53, True]
print('mixed values : ' +str(mixed_values))

# 5. Print out the values between the indexes 0 to 3
print(mixed_values[0:3])

# 6. Print out the value in index 6
#print(mixed_values[6])

# 8. BONUS : to the list from task 1 , Add the name ‘Alpha Romeo’ as the last item
# (Will be learned in the next lecture)
cars.append('Alpha Romeo')
print('added value : ' +str(cars))