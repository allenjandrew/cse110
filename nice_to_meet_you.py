print('')
print('Hello there! Welcome to the program!')
print('I\'m Bob, I\'ll be your coach throughout the course. Let\'s get you started!')
print('')
print('First off, what\'s your name?')
name = input().title()
if name == 'Bob':
    print('Hey! What a coincidence.. that\'s my name too! Nice!')
else:
    print(name + '! Hah! What an... interesting name.. well, I hope you like it, at least. Anyway, let\'s move on!')
print('')
print('My favorite color is red. How about yours?')
color = input().lower()
if color == 'red':
    print('Hey, we\'re pretty alike! Red\'s the best!')
else:
    print('Eww, really? I hate ' + color + '. But you do you.')
print('')
print('Well, it was nice to meet you, ' + name + '! I\'ll be here in VS Code to help you out whenever you need. Good luck!')
print('')