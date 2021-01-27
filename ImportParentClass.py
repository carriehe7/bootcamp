class Employee:

    def __init__(self, years_of_experience, position_name, name_of_employee):
        self.years_of_experience = years_of_experience
        self.position_name = position_name
        self.name_of_employee = name_of_employee


    def calculate_salary(self):

        base_salary = 2500
        calculated_salary = None

        if 0 <self.years_of_experience <=2:
            calculated_salary = base_salary + 1500

        elif 2 < self.years_of_experience <= 5:
            calculated_salary = base_salary + 2500

        elif self.years_of_experience > 5:
            calculated_salary = base_salary + 3500

        else:
            print("Wrong value inserted")

        print("Calculated salary is : %s" %calculated_salary)
        return calculated_salary

    def candidate_for_bonus(self, salary):

        salary_with_bonus = None

        if "front_end" in self.position_name:
            salary_with_bonus = salary * 1.1

        if self.years_of_experience > 2:
            salary_with_bonus = salary * 1.2

        print("The bonus for the employee in the position of %s is : %s" %(self.position_name, salary_with_bonus))