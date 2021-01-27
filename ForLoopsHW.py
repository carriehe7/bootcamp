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

    print('tax : ' +str(tax))
    print('income after healthcare reduction : ' +str(income_after_healthcare))
    print('\n')

    total_taxes = total_taxes + tax
print('total taxes : ' +str(total_taxes))