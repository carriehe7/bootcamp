# create new dictionary
new_employee = {'first name' : 'David', 'salary' : 10000, 'company' : 'Google'}

# print dictionary
print('print of dictionary : ' +str(new_employee))

# get cell 'value' - first way
print('get value of first name : ' +str(new_employee['first name']))

# get cell 'value' - second way
print('get value of salary : ' +str(new_employee.get('salary')))

# remove dictionary cell by using .pop()
new_employee.pop('salary')
print('remove dictionary cell : ' +str(new_employee))

# print out all keys of dictionary
print('print all keys of dictionary : ' +str(new_employee.keys()))

# print out all values of dictionary
print('print all values of dictionary : ' +str(new_employee.values()))

# use variable and place inside dictionary cell
job_title_value = 'developer'
new_dictionary = {'job_title' : job_title_value}
print('print new dictionary : ' +str(new_dictionary))