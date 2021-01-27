def salary_calc(salary, tax_reduction):
    employee_salary = salary * tax_reduction
    print('salary : ' +str(employee_salary))

salary_calc(10000, 0.98)
salary_calc(5000, 0.97)
salary_calc(2000, 0.95)

print('\n')

def my_function(x):
    return 5 * x

number = my_function(3)
print(number)

print('\n')

def my_function(country = 'Canada'):
    print('I am from ' + country)

my_function('Italy')
my_function()
my_function('Germany')

print('\n')

def phone_brands(brand3, brand1, brand2):
    print('The 3rd brand is : ' + brand3)

phone_brands(brand1= 'Apple', brand2= 'Xiaomi', brand3= 'LG')

print('\n')

def clothing_brands(*clothing_brands):
    print('The last company is : ' + clothing_brands[-1])

clothing_brands('Nike', 'Adidas', 'H&M')
clothing_brands('Nike', 'Adidas')

print('\n')

def my_function(**phone_info):
    print('The phone model is ' + phone_info['model'])

my_function(brand = 'Apple', model = 'iPhone_X')
my_function(brand = 'Apple', model = 'iPhone_X', year = '2015')