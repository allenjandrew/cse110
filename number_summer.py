from json.encoder import INFINITY


print('\nEnter a list of numbers. Type "0" when finished.\n')

numbers = []
number = int(input('Enter number here: '))
while number != 0:
    numbers.append(number)
    number = int(input('Enter number here: '))
    # print(numbers)

sum = 0
for item in numbers:
    sum += item
print(f'\nThe sum is: {sum}')

average = sum / len(numbers)
print(f'The average is: {average:.2f}')

largest = 0
for item in numbers:
    if item > largest:
        largest = item
print(f'The largest number is: {largest}')

smallest_pos = INFINITY
for item in numbers:
    if item > 0 and item < smallest_pos:
        smallest_pos = item
print(f'The smallest positive number is: {smallest_pos}')

sorted_numbers = sorted(numbers)
print('The numbers, sorted, are:')
for item in sorted_numbers:
    print(item)
print('')