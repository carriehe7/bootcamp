# if statements basics part 1
salary = 8000
if salary < 5000:
    print('my salary is too low, need to change my job')
else:
    print('salary is above 5000, okay for now')

age = 30
if age > 50:
    print('you are above 50. you are a senior developer for sure')
elif age > 40:
    print('your age is bigger than 40. you are a developer for some time, but if not, better late than never')
elif age > 35:
    print('so you are more than 35yo, I might guess you are a developer')
else:
    print("doesn't matter what age you are. let's code python")

# if statements basic part 2
age = 30
name = 'James'

# logical operator - 'and'
if age > 20 and name == 'James':
    print('my name is James and I am over 20')
else:
    print('default exit point')

# logical operator - 'or'
if age > 20 or name == 'James':
    print('my name is James and I am over 20')
else:
    print('default exit point')

# nested 'if' statement
married = True
if age > 20 and name == 'James':
    if married == True:
        print("good luck, it's gonna be a long happy ride")
    else:
        print('nested else')
else:
    print('parent else')