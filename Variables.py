# simple string example
short_string_variable = "Have a great week!"
print(short_string_variable)

# print first letter of string variable
first_letter_variable = 'New York City'[0]
print(first_letter_variable)

# mixed upper & lower case letter variable
mixed_letter_variable = 'ThIs Is A mIxEd VaRiAbLe'
print(mixed_letter_variable.lower())

# length of variable
print(len(mixed_letter_variable))

# use '+' sign inside print cmd
first_name = 'David'
print('first name is : ' +first_name)

# replace part of string
first_serial_number = 'ABC123'
print('changed serial number #1 : ' +first_serial_number.replace('123','456'))

# replace part of string 2x
second_serial_number = 'ABC123ABC'
print('changed serial number #2 : ' +second_serial_number.replace('ABC','ZZZ',2))

# take part of variable according to specific index range
range_of_indexes = second_serial_number[0:3]
print(range_of_indexes)

# adding spaces btwn multiple variables in print
first_word = 'Thank'
second_word = 'you'
third_word = '!'
print(first_word+' '+second_word+' '+third_word)