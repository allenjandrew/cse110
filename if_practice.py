number_1 = int(input('\nEnter an integer: '))
number_2 = int(input('Enter another integer: '))

if number_1 > number_2:
    print('\nThe first number is greater.')
else:
    print('\nThe first number is not greater.')

if number_1 == number_2:
    print('The numbers are equal.')
else:
    print('The numbers are not equal.')

if number_1 < number_2:
    print('The second number is greater.')
else:
    print('The second number is not greater.')

favorite_animal = input('\nWhat is your favorite animal? ')

if favorite_animal.lower() == 'dog':
    print('\nThat\'s my favorite animal too!\n')
else:
    print('\nOkay cool! My favorite animal is a dog.\n')
