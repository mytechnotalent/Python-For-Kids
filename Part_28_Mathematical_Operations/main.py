print(5 * (9 + 5) / 3 - 3)

# First: (9 + 5) = 14
# Second: 5 * 14 = 70
# Third: 70 / 3 = 23.33334
# Fourth: 23.33334 - 3 = 20.33334


first_number = int(input('Enter First Number: '))
second_number = int(input('Enter Second Number: '))

my_addition = first_number + second_number
my_subtraction = first_number - second_number
my_multiplication = first_number * second_number
my_division = first_number / second_number

print('Addition = {0}'.format(my_addition))
print('Subtraction = {0}'.format(my_subtraction))
print('Multiplication = {0}'.format(my_multiplication))
print('Division = {0}'.format(my_division))
print(type(my_division))

