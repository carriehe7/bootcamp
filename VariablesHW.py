# 1. Declare a string named “windows_serial_number” and give it the value “abc-def-ghi-jkl”
windows_serial_number = 'abc-def-ghi-jkl'

# 2. Create new 4 variables. Each variable will contain 3 letters out of the above ‘windows_serial_number’ variable. Use with a ‘new’ prefix in their name.
# hint: Use ‘index’ range, to extract exactly what you need from the ‘original’ variable from step 1
new_var1 = windows_serial_number[0:3]
new_var2 = windows_serial_number[4:7]
new_var3 = windows_serial_number[8:11]
new_var4 = windows_serial_number[12:15]
print(new_var1,new_var2,new_var3,new_var4)

# Use ‘replace’ action and set on each of the above new variables to be the following values : “aaa”, “bbb”, “ccc” , “ddd”.
# Meaning : new_partial_variable_a should have the value -> “aaa” , and so on..
new_var1 = new_var1.replace('abc','aaa')
new_var2 = new_var2.replace('def','bbb')
new_var3 = new_var3.replace('ghi','ccc')
new_var4 = new_var4.replace('jkl','ddd')
print(new_var1,new_var2,new_var3,new_var4)

# Create a new variable called ‘encoded_windows_serial_number’, which should be built of the new four variables divided with ‘-’
# hint : (encoded_windows_serial_number = “aaa-bbb-ccc-ddd”)
encoded_windows_serial_number = new_var1+'-'+new_var2+'-'+new_var3+'-'+new_var4
print(encoded_windows_serial_number)

# Print the new serial number and mention with plain text that this is the encoded serial number and add the new serial number to be printed
print('encoded serial number : ' +encoded_windows_serial_number)