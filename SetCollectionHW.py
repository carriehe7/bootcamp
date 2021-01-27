# 1. Create a 'set' collection of drinks with the following values:
# a. Cola
# b. Sprite
# c. Beer
# d. Water
# e. Soda
drinks = {'cola', 'sprite', 'beer', 'water', 'soda'}
print('drink collection : ' +str(drinks))

# 2. Add additional cell to set, with value 'Soda' (Question: What would be the output once we print it?)
drinks.add('soda')
print("add additional 'soda' : " +str(drinks))

# 3. Delete a 'Soda' cell out of set
drinks.remove('soda')
print("remove 'soda' : " +str(drinks))

# 4. Make a copy of set collections, name it drinks_2
drinks_2 = drinks.copy()
print('copy of set : ' +str(drinks_2))

# 5. ** BONUS : Print length of set collections (How many items we have inside?)
print('length of drinks collection : ' +str(len(drinks)))