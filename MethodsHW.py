# Part A
# Create a new method and call it ‘sorting’, that receives Arbitrary Arguments,
# and execute it 3 times with these variables passed to it :
# ● ‘Python’ & ‘Java’
# ● ‘Python’, ‘Java’, ’Go’
# ● ‘Python’, ‘JS’, ‘C++’
# Then, use a loop to find if “Java” is one of the values.
# Once “Java” is found, print each letter of it one-above-the-other in the output terminal.
def sorting(*programming_languages):
    for language in programing_languages:
        if language == 'Java':
            print('Java language found')

            for character in language:
                print(character)

        else:
            print('Java was not found')

sorting('Python', 'Java')
sorting('Python', 'Java', 'Go')
sorting('Python', 'JS', 'C++')

print('\n')

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
def tax_calculation(gross_salary, tax = 0.22):
    net_salary = gross_salary * (1-tax)
    print('net salary is : ' +str(net_salary))
    return net_salary

def salary_limit_tested(net_salary_var):
    if net_salary_var >= 5800:
        print('net salary is above 5800, it is : ' +str(net_salary_var))
    else:
        print('net salary is below 5800, it is : ' +str(net_salary_var))

net_salary_1 = tax_calculation(5000, 0.2)
salary_limit_tested(net_salary_1)
net_salary_2 = tax_calculation(6000, 0.22)
salary_limit_tested(net_salary_2)
net_salary_3 = tax_calculation(10000)
salary_limit_tested(net_salary_3)