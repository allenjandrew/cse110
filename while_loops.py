number = -1
print('')
while number < 0:
    number = int(input('Please type a positive number: '))
    if number < 0:
        print('Did... did you even go to preschool?')
print(f'Nice! The number is: {number}.\n')

can_have_candy = ''

while can_have_candy != 'yes':
    can_have_candy = input('Can I have a piece of candy? ').lower()
print('Thank you!!\n')