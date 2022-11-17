people_bare = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

print()
people_upd = []
for item in people_bare:
    print(item)
    person = item.split()
    person[1] = int(person[1])
    people_upd.append(person)

print()
youngest = ['', 1000]
for item in people_upd:
    print(f'{item[0]} is {item[1]} years old.')
    if item[1] < youngest[1]:
        youngest = item

print(f'\n{youngest[0]} is the youngest at {youngest[1]} years old.\n')