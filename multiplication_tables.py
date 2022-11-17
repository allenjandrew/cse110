number = int(input('\nHow many columns and rows do you want in your multiplication table? '))
spaces = len(str(number ** 2)) + 1

for i in range(1,number+1):
    for j in range(1,number+1):
        x = i*j
        print(f'{x:{spaces}}', end='')
    print('')
print('')