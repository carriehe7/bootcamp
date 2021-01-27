# 1. Create a dictionary of employees | Key = ‘name’ , ‘Value’ = ‘available working hours’
# employees = {
# "Jack": 6,
# "Russel": 10,
# "Keren": 2 }
employees = {'Jack' : 6, 'Russel' : 10, 'Keren' : 2}
print('employees dictionary : ' +str(employees))

# 2. The office is looking for an employee who can work between 5 - 8 hours. Use an ‘if’ statement that would check each cell to find that employee
# (Hint : ‘elif’)
if employees['Jack'] >= 5 and employees['Jack'] <= 8:
    print('Jack can work')
elif employees['Russel'] >= 5 and employees['Russel'] <= 8:
    print('Russell can work')
elif employees['Keren'] >= 5 and employees['Keren'] <= 8:
    print('Keren can work')
else:
    print('default exit point')

# 3. A. The office is looking for an employee to work the weekend. Also the manager wants someone who will work between 2 or 4 hours.
# B. The manager thinks that a girl named ‘Keren’ fits for this job.
# In addition, using a nested 'if’ what is the exact time she can spend at work.
# Don’t do anything inside the nested ‘if’, just add ‘default exit point - nested 'if’ at the nested ‘else'
if employees['Jack'] == 2 or employees['Jack'] == 4:
    print('Jack can work')
elif employees['Russel'] == 2 or employees['Jack'] == 4:
    print('Russel can work')
elif employees['Keren'] == 2 or employees['Keren'] == 4:
    print('Keren can work')
    if employees['Keren'] == 2:
        pass
    elif employees['Keren'] == 4:
        pass
    else:
        print('nested default exit point')
else:
    print('default exit point')