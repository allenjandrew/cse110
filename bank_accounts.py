account_names = []
account_balances = []
print('\nEnter the names and balances of bank accounts. Type QUIT when done.\n')
account_name = ''
while account_name != 'Quit':
    account_name = input('What is the name of this account? ').title()
    if account_name != 'Quit':
        account_balance = float(input('What is the balance? $'))
        account_names.append(account_name)
        account_balances.append(account_balance)

def print_acct_info():
    print('\nAccount Information:')
    for i in range(len(account_names)):
        print(f'{i}. {account_names[i]} - ${account_balances[i]:.2f}')
print_acct_info()

sum_accounts = 0
largest_balance = 0
largest_name = ''
for i in range(len(account_names)):
    sum_accounts += account_balances[i]
    if account_balances[i] > largest_balance:
        largest_balance = account_balances[i]
        largest_name = account_names[i]
avg_accounts = sum_accounts / len(account_names)

print(f'\nTotal: ${sum_accounts:.2f}')
print(f'Average: ${avg_accounts:.2f}')
print(f'Largest Balance: {largest_name} - ${largest_balance:.2f}')

should_update = ''
while should_update != 'no':
    should_update = input('\nWould you like to update an account\'s balance? (yes/no) ').lower()
    if should_update == 'yes':
        acct_to_update = int(input('Enter the index of the account you\'d like to update: '))
        updated_balance = float(input('What is the new balance? $'))
        account_balances[acct_to_update] = updated_balance
    print_acct_info()

print()