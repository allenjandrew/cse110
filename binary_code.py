# 39
# 19 r 1
# 9 r 1
# 4 r 1
# 2 r 0
# 1 r 0
# 100111

og_numb = input('\nEnter a number: ')
number = int(og_numb)
binary = ''
print('')
while number > 1: # commented print() functions are just to check if it's running right
    rem = number % 2
    # print(rem)
    binary = str(rem) + binary
    # print(binary)
    number = number // 2
    # print(number)
binary = '1' + binary
# print(binary)
print(f'\n{og_numb} in binary is written {binary}\n')