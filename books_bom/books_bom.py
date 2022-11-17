with open('books_bom.txt') as book_list:
    for line in book_list:
        stripped = line.strip()
        print(stripped)
