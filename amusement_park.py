print('\nWelcome to Rolling Thunder! Please enter the following.\n')

# First rider's information
first_age = float(input('What is the age of the first rider? '))
first_height = float(input('What is the height of the first rider (inches)? '))
if 12 <= first_age < 18:
    first_passport = input('Do you have a Golden Passport® (yes/no)? ')
    if first_passport == 'yes':
        first_age = 18 # This person is treated as if they were 18 years old.

# Is there a second rider?
second_yes_no = input('Is there a second rider (yes/no)? ').lower()
if second_yes_no == 'yes':
    hay_second = True # Creating a boolean variable
else:
    hay_second = False

# Second rider's information
second_age = 100
second_height = 100
if hay_second:
    second_age = float(input('What is the age of the second rider? '))
    second_height = float(input('What is the height of the second rider? '))
    if 12 <= second_age < 18:
        second_passport = input('Do you have a Golden Passport® (yes/no)? ')
        if second_passport == 'yes':
            second_age = 18 # This person is treated as if they were 18 years old.

# Checks to see if they can ride
if first_height < 36 or second_height < 36:
    can_ride = False # No one under 36 inches may ride.
elif not hay_second:
    if first_age >= 18 and first_height >= 62:
        can_ride = True # A single rider must be at least 18 years old and 62 inches tall.
elif hay_second:
    if first_age >= 18 or second_age >= 18:
        can_ride = True # A person under 18 may ride if accompanied by someone at least 18 years old. No height requirement.
    elif first_age >= 12 and first_height >= 52 and second_age >= 12 and second_height >= 52:
        can_ride = True # Two riders under 18 may ride if they are both at least 12 years old and 52 inches tall.
    elif (first_age >= 16 and second_age >= 14) or (first_age >= 14 and second_age >= 16):
        can_ride = True # Two riders under 18 may ride if one is at least 16 years old and the other is at least 14 years old.
else:
    can_ride = False # Any other combination of riders may not ride.

if can_ride:
    print('\nWelcome to the ride. Please be safe and have fun!\n')
else:
    print('\nSorry, you may not ride.\n')