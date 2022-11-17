print('\nEnter the following:\n')
vowels = ('A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u') # this will be used later
adjective1 = input('Adjective: ')
animal = input('Animal: ')
verb1 = input('Verb: ')
exclamation = input('Exclamation: ').capitalize()
verb2 = input('Verb: ')
verb3 = input('Verb: ')
noun1 = input('Noun: ')
adjective2 = input('Adjective: ')
famous_person = input('Name of famous person: ').title()
adjective3 = input('Adjective: ')
# check if adjective3 starts with a vowel, so the program knows if it should use "a" or "an" in the story
if adjective3.startswith(vowels):
    adjective3 = 'n ' + adjective3
else: adjective3 = ' ' + adjective3
noun2 = input('Noun: ')
woosh = input('Weird noise: ')
adjective4 = input('And one more adjective: ')
verb4 = input('Lastly, a past-tense verb: ')
# alright, we're ready to see what the user has come up with!
generate = input('\nPress enter to generate your story! ')
print(f'\nThe other day something crazy happened at school. It all started when I saw')
print(f'a very {adjective1} {animal} {verb1} down the hallway. "{exclamation}!" I yelled. But all')
print(f'I could think to do was to {verb2} over and over. Miraculously, that caused')
print(f'it to stop, but not before it tried to {verb3} right in front of my {noun1}.')
print(f'I was so {adjective2} that I couldn\'t react. Luckily, {famous_person} broke through')
print(f'the window with a{adjective3} {noun2} and threw it at the {animal}. With a great')
print(f'{woosh}, {famous_person}, the {noun2}, and the {animal} disappeared in a')
print(f'flash of {adjective4} light. I thought I was going crazy, so I went home')
print(f'and {verb4} for the rest of the afternoon.\n')