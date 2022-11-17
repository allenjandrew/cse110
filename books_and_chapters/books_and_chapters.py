print()
books_list = []
max_chapters = 0
volumes = []

with open('books_and_chapters.txt') as books_info:
    for line in books_info:
        line = line.strip()
        line_info = line.split(':')
        line_info[1] = int(line_info[1])
        print(f'Scripture: {line_info[2]}, Book: {line_info[0]}, Chapters: {line_info[1]}')
        if line_info[1] > max_chapters:
            max_chapters = line_info[1]
            max_info = line_info
        books_list.append(line_info)
        if line_info[2] not in volumes:
            volumes.append(line_info[2])
print(f'\nThe largest book in all of Scripture is {max_info[0]} in the {max_info[2]} with {max_info[1]} chapters.')

print('\nWhich volume of Scripture would you like to learn more about?')
for i in range(len(volumes)):
    print(f'{i+1}. {volumes[i]}')
user_choice = volumes[int(input('Enter the number of the selected volume: '))-1]
max_chapters_user = 0

for book_info in books_list:
    if book_info[2] == user_choice and book_info[1] > max_chapters_user:
        max_chapters_user = book_info[1]
        max_info_user = book_info
print(f'\nThe largest book in the {user_choice} is {max_info_user[0]} with {max_info_user[1]} chapters.')

print()