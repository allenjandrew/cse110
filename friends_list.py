print('\nPlease enter the names of your friends. When you\'ve finished, type "end".\n')
friends = []

friend = input()
while friend.lower() != 'end':
    friends.append(friend)
    friend = input()

if len(friends) == 0:
    print('\nThat\'s rough, man. I\'d hate to be you.\n')

elif len(friends) == 1:
    print(f'\nYour friend is {friends[0]}.\n')

elif len(friends) == 2:
    print(f'\nYour friends are {friends[0]} and {friends[1]}.\n')

else:
    print('\nYour friends are ', end='')
    for person in friends:
        if friends.index(person) == len(friends) - 1:
            print(f'and {person}.\n')
        else:
            print(f'{person}, ', end='')