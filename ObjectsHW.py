"""
Create an object class, class methods, and instances:
    Class: Please create a 'Car' class and an '__init__' method that would receive 1 'list' type argument
    Object of an instance: Create 2 object instances: audi_a3, ford_focus
    Properties: The instance of an object would receive a list, which will  contain the following variables:
        List's Legend: year of release, current car price, name, door's closed status
            ford_focus_list = [2005, 5000, 'ford_focus', True]
            audi_a3_list = [2011, 15000, 'audi_a3', False]

Class method #1 - insurance_price():
Calculate the insurance_price by using these conditions:
    a. If the year of release is btwn 2010 and 2020 and the current price is btwn 6000 and 17000,
        the insurance would be 5% of the car's worth
    b. For every other parameter, the insurance would be 7% of the car's worth

Class method #2 - doors_status():
Print whether the doors are closed or not. The last value of the 'list' indicates it.
If the value is 'True', it means the doors are closed.

Class method #3 - car_data():
Print car's data in the following structure:
"The car model is ___, it was released at the year ___ and it costs ___'
Use string formatting approach for the print

Execution:
Execute all 3 methods for each instance of an object
"""

class Car():
    def __init__(self, car_data_list):
        self.car_data_list = car_data_list

    def insurance_price(self):
        year_of_release = self.car_data_list[0]
        car_price = self.car_data_list[1]
        model = self.car_data_list[2]

        if 2010 <= year_of_release <= 2020 and 6000 <= car_price <= 17000:
            insurance = car_price * 0.05
        else:
            insurance = car_price * 0.07

        print('insurance for model %s is %s' % (model, insurance))

    def doors_status(self):
        doors_status = self.car_data_list[-1]

        if doors_status == True:
            print('Doors are closed')
        elif doors_status == False:
            print('Doors are opened')
        else:
            print('Wrong value inserted')

    def get_car_data(self):
        print('The car model is %s, it was released in year %s and costs %s'
              % (self.car_data_list[2], self.car_data_list[0], self.car_data_list[1]))

ford_focus_list = [2005, 5000, 'ford_focus', True]
ford_focus_instance = Car(ford_focus_list)
ford_focus_instance.insurance_price()
ford_focus_instance.doors_status()
ford_focus_instance.get_car_data()

print('\n')

audi_a3_list = [2011, 15000, 'audi_a3', False]
audi_a3_instance = Car(audi_a3_list)
audi_a3_instance.insurance_price()
audi_a3_instance.doors_status()
audi_a3_instance.get_car_data()