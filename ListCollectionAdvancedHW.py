# 1. Create a list of employees -
# a. Adam
# b. John
# c. Greg
# d. Danna
# e. Ashly
employees = ['Adam', 'John', 'Greg', 'Danna', 'Ashly']
print('employees : ' +str(employees))

# 2. Print the length of list
print('length of employee list : ' +str(len(employees)))

# 3. John quit job and new guy came in, named 'Jack'. Add him to list, instead of 'John' into index '1'
employees[1] = 'Jack'
print('new employee : ' +str(employees))

# 4. Another guy joined team, 'Mavrik'. Add him to index '3' (do not remove old member of team)
employees.insert(3,'Mavrik')
print('add Mavrik : ' +str(employees))

# 5. Seems that Mavrik was added to wrong place
# a. Remove him from list
# b. Then add him to be last in list
employees.remove('Mavrik')
print('remove Mavrik : ' +str(employees))
employees.append('Mavrik')
print('add Mavrik at end : ' +str(employees))

# 6. Mavrik did not fit into team, skipped work and boss didn't like it, so he fired him. Remove him from list (use pop())
employees.pop()
print('remove Mavrik : ' +str(employees))

#7. BONUS : search google and sort list by 'abc'
print('sorted list : ' +str(sorted(employees)))
