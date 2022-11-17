print('')

james = input('Please enter FIRST_NAME : ').capitalize()
bond = input('Please enter LAST_NAME : ').capitalize()

# james = input('Please enter FIRST_NAME : ')
# bond = input('Please enter LAST_NAME : ')

print('')

# lady = '"..and you are, um ... Mister - "'
# agent = '"{1}, {0} {1}."'.format(james.capitalize(), bond.capitalize())
# print(lady)
# print(agent)

lady = '"..and you are, um ... Mister - "'
agent = '"{1}, {0} {1}."'.format(james, bond)
print(lady)
print(agent)

# This is if I were to use the original method of concatenating strings.
# print('"..and you are, um ... Mister - "')
# print('"' + bond + ', ' + james + ' ' + bond + '."')

print('')