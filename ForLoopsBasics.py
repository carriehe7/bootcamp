numbers_a = [1, 2, 3]

numbers_a[0] = numbers_a[0] * 5
numbers_a[1] = numbers_a[1] * 5
numbers_a[2] = numbers_a[2] * 5

print('WRONG WAY')
print(numbers_a[0])
print(numbers_a[1])
print(numbers_a[2])

print('\n') # skips one empty line below

numbers_b = [1, 2, 3]
print('RIGHT WAY')

for cell in numbers_b:
    cell = cell * 5
    print(cell)