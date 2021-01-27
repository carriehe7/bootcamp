# 1. Create 6 variables
# a. Gross salary - 10000
# b. Health insurance - 430.99
# c. Rent - 1200
# d. Food - 400.5
# e. Salary tax - 20%
# f. (Use in task 3) Donation to the poor (out of net salary) = 10%
gross_salary = 10000
health_insurance = 430.99
rent = 1200
food = 400.5
salary_tax = 0.2
donation = 0.1

# 2. Calculate your net salary and print it
tax = gross_salary * salary_tax
net_salary = gross_salary - tax - health_insurance - rent - food
print('net salary : ' +str(net_salary))

# 3. Calculate the amount of donation you give the poor
donation_amount = net_salary * donation
print('donation amount: ' +str(donation_amount))

# 4. Round the limit of the result from section 3, into 2 numbers after decimal.
# Try to find it using google
# (Use the phrase : ‘python limit numbers after decimal’)
donation_amount_rounded = round(donation_amount,2)
print('rounded amount : ' +str(donation_amount_rounded))

donation_amount_rounded2 = '%.2f' % donation_amount
print('rounded amount : ' +str(donation_amount_rounded2))