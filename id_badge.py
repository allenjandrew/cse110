print('\nPlease enter the following information:\n')
first_name = input('First name: ').title()
last_name = input('Last name: ').upper()
email = input('Email address: ').lower()
phone = input('Phone number: ')
job_title = input('Job title: ').title()
id = input('ID number: ')
hair = input('Hair color: ').capitalize()
eyes = input('Eye color: ').capitalize()
month = input('Starting month: ').capitalize()
training = input('Completed advanced training (yes/no): ').capitalize()
if training == 'Yes':
    training = 'Completed'
elif training == 'No':
    training = 'Not completed'
# Not to be printed. Will be saved in database
marital_status = input('Relationship status: ').capitalize()
social_security = input('Social security number: ')

print('\nPrinting ID card...')
print('--------------------------')
print(f'{last_name}, {first_name}\n{job_title}\nID: {id}\n\n{email}\n{phone}\n')
print(f'Hair: {hair}         Eyes: {eyes}\nStarted in: {month}    Training: {training}')
print('--------------------------\n')
print('ID card printed.\n')