from microbit import display

length = float(input('Enter length: '))
width = float(input('Enter width: '))

square_footage = length * width

print('Your room size is {0} square feet.'.format(square_footage))
display.scroll('Your room size is {0} square feet.'.format(square_footage))
