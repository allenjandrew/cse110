shopping_list = []

item = input('\nPlease enter the items of the shopping list (type QUIT to finish).\nItem: ').title()

while item != 'Quit':
    shopping_list.append(item)
    item = input('Item: ').title()

print('\nThe shopping list is:')
for thing in shopping_list:
    print(thing)

print('\nThe shopping list with indexes is:')
for i in range(len(shopping_list)):
    print(f'{i}. {shopping_list[i]}')

change_num = int(input('\nWhich item would you like to change? '))
new_item = input('What is the new item? ').title()
shopping_list[change_num] = new_item

print('\nThe shopping list with indexes is:')
for i in range(len(shopping_list)):
    print(f'{i}. {shopping_list[i]}')

print()