"""
We will create 2 classes :
1. Parent class - Employee
2. Child class - Programmer

Employee class would have :
★ #1 property - self.years_of_experience [Integer]
★ #2 property - self.position_name [String]
★ #3 property - self.employee_name [String]

❖ #1 method - calculated_salary()
Create a ‘calculated_salary’ variable based these parameters:
- Base salary is 2500
- Between 0-2 years of experience, including 2, salary raises by 1500
- Between 2-5 years of experience, including 5. salary raises by 2500
- Above 5 years of experience salary raises by 3500
- Take into consideration if wrong value is inserted
- Print the ‘calculated_salary’
- Return the 'calculated salary'

❖ #2 method - candidate_for_bonus()
Would calculate the salary based on 2 properties :
position_name and years_of_experience.
- Pass the calculated_salary variable, and add bonus on top of it
> Create a calculation based on the following parameters <
- A bonus of 0.1 out of the monthly calculated salary will be handed to
all ‘front_end’ developers
(Check hint at the end of the page)
- An additional bonus 0f 0.2 will be given to all employee who has above
2 years of experience (Employee cannot get 2 bonuses)

Programmer class would have :
● Should inherit all methods and properties
● #1 method - print ‘name of employee’ , ‘position’, in your own sentence.
(Use string formatting)

Create 2 instances:
1. junior_python_programmer : which will get the values : 1, “front-end”,
“Joseph”
2. senior_devops : which will get the values : 6, “senior_devops”, “Dan”

Hint :
To check whether a certain phrase appears in another phrase,
by using an ‘if’, use this template : if 'abc’ in ‘abcd’.
That will check whether ‘abc’ appears in ‘abcd’ and return a ‘True’ or ‘False’
value
"""

class Employee:
    def __init__(self, years_of_experience, position_name, employee_name):
        self.years_of_experience = years_of_experience
        self.position_name = position_name
        self.employee_name = employee_name

    def calculated_salary(self):
        base_salary = 2500
        calculated_salary = None

        if 0 < self.years_of_experience <= 2:
            calculated_salary = base_salary + 1500
        elif 2 < self.years_of_experience <= 5:
            calculated_salary = base_salary + 2500
        elif self.years_of_experience > 5:
            calculated_salary = base_salary + 3500
        else:
            print('Wrong value inserted')

        print('Calculated salary is %s' % calculated_salary)
        return calculated_salary

    def candidate_for_bonus(self, salary):
        salary_with_bonus = None

        if 'front-end' in self.position_name:
            salary_with_bonus = salary * 1.1
        elif self.years_of_experience > 2:
            salary_with_bonus = salary * 1.2

        print('The bonus for employees as position %s is %s' % (self.position_name, salary_with_bonus))

class Programmer(Employee):
    def __init__(self, years_of_experience, position_name, employee_name):
        super().__init__(years_of_experience, position_name, employee_name)
        self.years_of_experience = years_of_experience
        self.position_name = position_name
        self.employee_name = employee_name

    def print_info(self):
        print('The position of employee, %s, is %s' % (self.employee_name, self.position_name))

junior_python_programmer = Programmer(1, 'front-end', 'Joseph')
calculated_salary_programmer = junior_python_programmer.calculated_salary()
junior_python_programmer.candidate_for_bonus(calculated_salary_programmer)
junior_python_programmer.print_info()

print('\n')

senior_devops = Programmer(6, 'senior_devops', 'Dan')
calculated_salary_devops = senior_devops.calculated_salary()
senior_devops.candidate_for_bonus(calculated_salary_devops)
senior_devops.print_info()