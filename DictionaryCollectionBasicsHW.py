# 1. Create a dictionary about Alex: Alex = {"Age": 32 , "Married" : “Yes”, "Kids": 3}
alex = {'age' : 32, 'married' : 'yes', 'kids' : 3}
print("Alex's dict : " +str(alex))

# 2. Extract all values of the dictionary, and assign them into simple variables
# (Choose variables type, according the value’s type of input)
age = alex['age']
married_status = alex['married']
number_of_kids = alex['kids']
print("print of 'age' value : " +str(age))
print("print of 'married_status' value : " +(married_status))
print("print of 'number_of_kids' value : " +str(number_of_kids))

# 3. ( <Challenge> ) Search in Google, how to change a value of a dictionary
# Try the phrase : “Python update value of dictionary”
# (Note : If you get into trouble, scroll down to Page 2 of this document, there you would find the answer)

# 4. Alex had a birthday and now is 33, update the value that belongs to the key = ‘Age’
age_dictionary = {'age' : 33}
alex.update(age_dictionary)
print('update age : ' +str(alex))

# 5. Once Alex became 33, a little girl joined his family, update the ‘Kids’ key value into ‘4’
kids_dictionary = {'kids' : 4}
alex.update(kids_dictionary)
print('update # of kids : ' +str(alex))

# 6. Print out the values of the dictionary
print('values of dict : ' +str(alex.values()))

# 7. Print out the keys of the dictionary
print('keys of dict : ' +str(alex.keys()))