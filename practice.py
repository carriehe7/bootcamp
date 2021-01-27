# 1. Create a dictionary of employees | Key = ‘name’ , ‘Value’ = ‘available working hours’
# employees = {
# "Jack": 6,
# "Russel": 10,
# "Keren": 2 }
employees = {'Jack': 6, 'Russel': 10, 'Keren': 2}
print(employees)

# 2. The office is looking for an employee who can work between 5 - 8 hours.
# Use an ‘if’ statement that would check each cell to find that employee (Hint : ‘elif’)
if employees['Jack'] >= 5 and employees['Jack'] <= 8:
    print('Jack can work')
elif employees['Russel'] >= 5 and employees['Russel'] <= 8:
    print('Russel can work')
elif employees['Keren'] >= 5 and employees['Keren'] <= 8:
    print('Keren can work')
else:
    print('no one can work')

# 3. A. The office is looking for an employee to work the weekend. Also the manager wants someone who will work between 2 or 4 hours.
# B. The manager thinks that a girl named ‘Keren’ fits for this job.
# In addition, using a nested 'if’ what is the exact time she can spend at work.
# Don’t do anything inside the nested ‘if’, just add ‘default exit point - nested 'if’ at the nested ‘else'
if employees['Jack'] == 2 or employees['Jack'] == 4:
    print('Jack can work')
elif employees['Russel'] == 2 or employees['Russel'] == 4:
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

"""
Congrats! You started working as an algorithm developer for the IRS (Internal Revenue Service).
Your Team Leader gave you the first assignment which is to create a formula for collecting tax.
You should stick to the following rules:
1. Businesses with gross incomes in between 1 - 2k will pay 5% tax.
2. Businesses with gross incomes in between 2k - 5k will pay 10% tax.
3. Businesses with gross incomes in between 5k - 15k will pay 15% tax.
4. Above 15k , will all pay 17% tax from gross income.
5. All businesses will pay an additional 2% for healthcare out of net income as well, after tax reduction, and just print it.
6. Also calculate the total tax you got from the given 10 business in the list (exclude healthcare)
7. businesses_list = [1500, 2542, 2001, 3500, 5300, 5555, 17000, 21000, 10, 15001]
"""
businesses_list = [1500, 2542, 2001, 3500, 5300, 5555, 17000, 21000, 10, 15001]
total_taxes = 0

for income in businesses_list:
    if income >= 1000 and income <= 2000:
        tax = income * 0.05
    elif income >= 2000 and income <= 5000:
        tax = income * 0.1
    elif income >= 5000 and income <= 15000:
        tax = income * 0.15
    else:
        tax = income * 0.17

    net_income = income - tax
    income_after_healthcare = net_income * 0.98
    print(income_after_healthcare)

    total_taxes = total_taxes + tax

# Part A
# 1. Create a list of ‘ages’ with the following values: 5 , 6, 24, 32, 21, 70
ages = [5 , 6, 24, 32, 21, 70]

# 2. The condition of the while loop should look for ages under 30

# 3. Each cycle in the while loop, should get a value out of the list
# (Hint : Use a counter)
counter = 0
while ages[counter] < 30:

# 4. Print each tested cell inside the loop
    print(ages[counter])
    counter += 1

# 5. Once the condition is false, print the cell that caused it
print(ages[counter])

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
        print(ages[counter])
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
    print(ages[counter])
    counter += 1

# 3. If the loop reaches to the number 70, it should run an ‘else’ part with the print :
# “I’m inside ‘else’ because of *listCell*’
else:
    print("I'm inside 'else' because of number : " +str(ages[counter]))

# Part A
# Create a new method and call it ‘sorting’, that receives Arbitrary Arguments,
# and execute it 3 times with these variables passed to it :
# ● ‘Python’ & ‘Java’
# ● ‘Python’, ‘Java’, ’Go’
# ● ‘Python’, ‘JS’, ‘C++’
# Then, use a loop to find if “Java” is one of the values.
# Once “Java” is found, print each letter of it one-above-the-other in the output terminal.
def sorting(*program_lang):
    for language in program_lang:
        if language == 'Java':
            print('Java found')

            for character in language:
                print(character)
        else:
            print('Java not found')

sorting('Python', 'Java')
sorting('Python', 'Java', 'Go')
sorting('Python', 'Java', 'C++')

# Part B
# 1. Create a method, and call it ‘tax_calculation’, it would get 2 variables : gross_salary, tax.
# Notice, that if no ‘tax’ variable is passed into the method, it should use 0.22 by default
# 2. Execute it 3 times with these values :
# ● 5000, 0.2
# ● 6000, 0.22
# ● 10000
# 3. Calculate the the ‘net_salary’ by reducing the ‘tax’ out of the ‘gross_salary’,
# and return it at the end of the method
# 4. Create a second method and call it ‘salary_limit_tester’, it should receive a
# ‘net_salary’ variable and check whether it is above or below ‘5800’
# 5. Whether the salary is above or below 5800, state it in a print, and mention
# the value of the tested salary
def tax_calc(gross_salary, tax = 0.22):
    net_salary = gross_salary * (1-tax)
    print(net_salary)
    return net_salary

def salary_limit_tester(net_salary_var):
    if net_salary_var >= 5800:
        print(net_salary_var)
    else:
        print(net_salary_var)

net_salary_1 = tax_calc(5000, 0.2)
salary_limit_tester(net_salary_1)
net_salary_2 = tax_calc(6000, 0.22)
salary_limit_tester(net_salary_2)
net_salary_3 = tax_calc(10000)
salary_limit_tester(net_salary_3)