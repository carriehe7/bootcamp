# Take the following pre-prepared parts of code, that will raise exception / errors once running them.
# Your mission is to use a ‘try-except’ statement to overcome the code from failing.
# For example - if using a variable without it being declared first, assign any value to it in the except part.
# 1. x=5
# print ("The number is : " +x)
# 2. x + 5
# 3. list = [1,2,3,4]
# print(list[6])

x = 5
try:
    print('The number is : ' +x)
except:
    print('casting was not done for print of x')
    print('The number is : %s' % x)

print('\n')

try:
    y + 5
except:
    y = 1
    print('y variable was not defined')
    result = y + 5
    print(result)

print('\n')

list = [1,2,3,4]
try:
    print(list[6])
except:
    print('index 6 not found since only 3 is available')
    print(list[3])