reusable_data = []
show_all = False

with open('life_expectancy.csv') as life_data:
    for line in life_data:
        clean_line = line.strip()
        line_data = clean_line.split(',')
        if line_data[0] != 'Entity':
            line_data[3] = float(line_data[3])
            reusable_data.append(line_data)

print('\nThank you for using the Life Expectancy Data Analyzer.')
print('Please enter the year and/or country you\'d like to see data from (you can leave one or both inputs blank).')
user_year = input('Year: ')
user_country = input('Country: ').title()
if (user_year == '' and user_country != '') or (user_year != '' and user_country == ''):
    if input(f'Show all data from {user_year}{user_country} (yes/no)? ').lower() == 'yes':
        show_all = True

counter = 0
sum_ = 0
shortest_life = 999
longest_life = 0
year_data = []
country_data = []
line_prev = ['country','code','year',0]
largest_drop = ['year1',0,'year2',0,0]
largest_rise = ['year1',0,'year2',0,0]
prev_data = False
next_data = False

for i in range(len(reusable_data)):
    line = reusable_data[i]
    if user_year == '' and user_country == '': # The user didn't input anything
        counter += 1
        sum_ += line[3]
        if line[3] < shortest_life: # Find shortest life expectancy overall
            shortest_life = line[3]
            shortest_data = line
        if line[3] > longest_life: # Find longest life expectancy overall
            longest_life = line[3]
            longest_data = line

    elif user_country == '': # The user only input a year
        if line[2] == user_year: # Find data for only that year
            counter += 1
            sum_ += line[3]
            year_data.append(line)
            if line[3] < shortest_life: # Find shortest life expectancy for the year
                shortest_life = line[3]
                shortest_data = line
            if line[3] > longest_life: # Find longest life expectancy for the year
                longest_life = line[3]
                longest_data = line

    elif user_year == '': # The user only input a country
        if line[0].title() == user_country: # Find data for only that country
            counter += 1
            sum_ += float(line[3])
            country_data.append(line)
            if line[3] < shortest_life: # Find shortest life expectancy for the country
                shortest_life = line[3]
                shortest_data = line
            if line[3] > longest_life: # Find longest life expectancy for the country
                longest_life = line[3]
                longest_data = line
            if (line_prev[3] - line[3]) > largest_drop[4] and line_prev[3]:
                largest_drop = line_prev[2],line_prev[3],line[2],line[3],(line_prev[3] - line[3])
            if (line[3] - line_prev[3]) > largest_rise[4] and line_prev[3]:
                largest_rise = line_prev[2],line_prev[3],line[2],line[3],(line[3] - line_prev[3])
            line_prev = line

    else: # The user input both a year and a country
        if line[0].title() == user_country and line[2] == user_year: # Find data for that country in that year
            specific_data = line
            if reusable_data[i-1][0] == user_country:
                prev_data = reusable_data[i-1] # Find data for previous year
                prev_diff = specific_data[3] - prev_data[3] # Find difference from previous to current years
                if prev_diff > 0:
                    prev_incr = 'increased'
                else:
                    prev_incr = 'decreased'
            if reusable_data[i+1][0] == user_country:
                next_data = reusable_data[i+1] # Find data for next year
                next_diff = next_data[3] - specific_data[3] # Find difference from current to previous years
                if next_diff > 0:
                    next_incr = 'increased'
                else:
                    next_incr = 'decreased'
            counter = 1 # To prevent division by zero

average_life = sum_ / counter
print()

if user_year == '' and user_country == '':
    print('Overall Statistics:')
    print(f'The highest life expectancy overall was in {longest_data[2]} in {longest_data[0]} at {longest_data[3]:.2f} years.')
    print(f'The lowest life expectancy overall was in {shortest_data[2]} in {shortest_data[0]} at {shortest_data[3]:.2f} years.')

elif user_country == '':
    print(user_year + ' Statistics:')
    print(f'The highest life expectancy in {user_year} was in {longest_data[0]} at {longest_data[3]:.2f} years.')
    print(f'The lowest life expectancy in {user_year} was in {shortest_data[0]} at {shortest_data[3]:.2f} years.')
    print(f'The average life expectancy across all countries in {user_year} was {average_life:.2f} years.')
    if show_all:
        print(f'Worldwide data for {user_year}:')
        for line in year_data:
            print(f'{line[0]}: {line[3]:.2f} years')

elif user_year == '':
    print(user_country + ' Statistics:')
    print(f'The highest life expectancy in {user_country} was in {longest_data[2]} at {longest_data[3]:.2f} years.')
    print(f'The lowest life expectancy in {user_country} was in {shortest_data[2]} at {shortest_data[3]:.2f} years.')
    print(f'The largest drop in life expectancy in {user_country} happened between {largest_drop[0]} and {largest_drop[2]} with a drop of {largest_drop[4]:.2f} years.')
    print(f'The largest rise in life expectancy in {user_country} happened between {largest_rise[0]} and {largest_rise[2]} with a rise of {largest_rise[4]:.2f} years.')
    print(f'The all-time average life expectancy in {user_country} was {average_life:.2f} years.')
    if show_all:
        print(f'All-time data for {user_country}:')
        for line in country_data:
            print(f'{line[2]}: {line[3]:.2f} years')

else:
    print(f'In {user_country} in {user_year}, the life expectancy was {specific_data[3]:.2f}.')
    if prev_data and next_data:
        print(f'The life expectancy {prev_incr} from {prev_data[3]:.2f} the previous year, and {next_incr} to {next_data[3]:.2f} the next year.')
    elif prev_data:
        print(f'The life expectancy {prev_incr} from {prev_data[3]:.2f} the previous year.')
    elif next_data:
        print(f'The life expectancy {next_incr} to {next_data[3]:.2f} the next year.')
print()