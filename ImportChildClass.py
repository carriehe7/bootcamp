from ImportParentClass import Employee


class Programmer(Employee):

    def __init__(self, years_of_experience, position_name, name_of_employee):
        super().__init__(years_of_experience, position_name, name_of_employee)
        self.years_of_experience = years_of_experience
        self.position_name = position_name
        self.name_of_employee = name_of_employee

    def print_data(self):
        print("The employee %s works as a %s in our company " %(self.name_of_employee, self.position_name))