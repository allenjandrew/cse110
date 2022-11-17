import random
number = random.randint(1,100)
# print(number)

print('\nThe magic number is between 1 and 100!')

guess = int(input('\nWhat is your guess? '))
tries = 1

while guess != number:
    if guess > number:
        guess = int(input('Try a smaller number. '))
    elif guess < number:
        guess = int(input('Try a larger number. '))
    tries += 1

whelp = ''
if tries >= 12:
    whelp = ' Better luck next time!'
elif tries <= 6:
    whelp = ' That\'s impressive!'

print(f'Nice job! It took you {tries} tries to get it.{whelp}\n')