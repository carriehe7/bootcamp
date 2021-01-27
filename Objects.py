class Employee:
    def __init__(self, name, salary, attendance):
        self.name = name
        self.salary = salary
        self.attendance = attendance

    def attendance_check(self):
        print('' +self.name + "'s attendance " + 'status is : ' +str(self.attendance))

    def show_employee_details(self):
        print('Name : ', self.name, ', Salary : ', self.salary)

sara = Employee('sara', '1000', False)
sara.show_employee_details()

michael = Employee('michael', '3000', True)
michael.show_employee_details()
michael.attendance_check()

print('\n')

class Building():
    def __init__(self, season_in_year, apt_number, apt_size):
        self.season_in_year = season_in_year
        self.apt_number = apt_number
        self.apt_size = apt_size

    def rental_calc(self):
        base_price_per_month = 2000
        season_price_buffer = 0

        if self.season_in_year == 'summer':
            season_price_buffer = 1.5
        elif self.season_in_year == 'winter':
            season_price_buffer = 1.1
        elif self.season_in_year == 'spring':
            season_price_buffer = 1.4
        elif self.season_in_year == 'fall':
            season_price_buffer = 1.3
        else:
            season_price_buffer = None

        if self.apt_size > 130:
            season_price_buffer += 0.1

        total_rent_price = base_price_per_month * season_price_buffer
        # string formatting
        print('The buffer is %s ' % season_price_buffer)
        print('The total price is %s ' % total_rent_price)

        return total_rent_price

    def monthly_maintenance_pay(self, rent_price):

        maintenance = 0

        if rent_price > 3000:
            maintenance = 100
        else:
            maintenance = 50

        print('The maintenance is %s ' % maintenance)

# creation of instance of object 1
lease_contract_1 = Building('summer', 4, 135)

# methods execution
rent_price_1 = lease_contract_1.rental_calc()
lease_contract_1.monthly_maintenance_pay(rent_price_1)

print('\n')

# creation of instance of object 2
lease_contract_2 = Building('spring', 6, 100)

# methods execution
rent_price_2 = lease_contract_2.rental_calc()
lease_contract_2.monthly_maintenance_pay(rent_price_2)
