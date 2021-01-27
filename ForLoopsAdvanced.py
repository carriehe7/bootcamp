for x in range(6):
    print(x)

print('\n')

for x in range(3, 7):
    print(x)

print('\n')

for x in range(3, 12, 3):
    print(x)

print('\n')

""" 
Guidelines for bonuses
1. I want you to build a formula for bonuses
2. Employees are placed in cells by their work ethic
3. Give each employee a bonus which will be based on his place in list, multiply by 100 (place * 100)
4. The boss said to give bonus by jumping +3 each time in list
5. The boss said that the first employee (cell index 0) does not deserve any bonus
"""

salary = [1000,2000,3000,4000,5000,6000,7000,8000,9000]

for place in range(0, 9, 3):
    if place == 0:
        pass
    else:
        salary_with_bonus = salary[place] + place * 100
        print(salary_with_bonus)