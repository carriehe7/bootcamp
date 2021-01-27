# 1. Create a nested dictionary of building attendants, the building has 3 apartments on 2 floors:
# a. Parent Key 1 : floor_1
# b. Parent Key 2 : floor_2
# c. Under parent key 1 - insert a nested 2 cells,
# - ‘first_apartment’ where ‘Rachel’ lives.
# - ‘second_apartment’ which ‘Jeen’ lives
# d. Under parent key 2 - insert a nested cell of the ‘third_apartment’ where ‘Jack’ lives.
building_attendants = {'floor_1' : {'first_apartment' : 'Rachel','second_apartment' : 'Jeen'},
                       'floor_2' : {'third_apartment' : 'Jack'}}
print('building attendants : ' +str(building_attendants))

# 2. Print all nested cell items of the 1st floor
print('nested cells in 1st floor : ' +str(building_attendants['floor_1']))

# 3. Print out the resident in the ‘second_apartment’
print('resident in 2nd apartment : ' +str(building_attendants['floor_1']['second_apartment']))

# 4. The building owner managed to build an additional apartment on the second floor, and a new resident moved to the new 4th apartment
# - her name is Carroll, Add her to the dictionary.
building_attendants['floor_2']['fourth_apartment'] = 'Carroll'
print('add new resident : ' +str(building_attendants))

# 5.(Advanced) - The building owner decided to let his daughter live in the first apartment, so it would not be leased any more, delete it from the dictionary.
# Hint : Use the same method used in the 2nd assignment, in order to delete the exact ‘value'
building_attendants['floor_1'].pop('first_apartment')
print('remove 1st apartment : ' +str(building_attendants))