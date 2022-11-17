age_current_string = input('\nHow old are you? ')
age_future_number = int(age_current_string) + 1
print(f'On your next birthday, you will be {age_future_number} years old.')
eggs_carton_string = input('\nHow many egg cartons do you have? ')
eggs_total_number = int(eggs_carton_string) * 12
print(f'Wow! You have a total of {eggs_total_number} eggs!')
cookies_string = input('\nHow many cookies are there? ')
if cookies_string == '0':
    print('Rough bro... don\'t worry, I think I might have a couple around here somewhere.. as long as Chrome didn\'t block them all, hehe.\n')
else:
    friends_string = input('How many friends do you have? ')
    if friends_string == '0':
        print('Oh! Awkward... well I guess you can have all of them for yourself then.. Sorry!\n')
    else:
        cookies_per_friend_number = int(cookies_string) / (int(friends_string) + 1) # adding one to include the user
        print(f'Great! Everybody gets {cookies_per_friend_number} cookies. Enjoy!\n')