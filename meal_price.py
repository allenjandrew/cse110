# Inputs
kids_meal = float(input('\nWhat is the price of a Kids\' Meal? $'))
adult_meal = float(input('What is the price of an adult\'s meal? $'))

num_kids = float(input('\nHow many children are there? '))
num_adults = float(input('How many adults are there? '))

drink_total = 0
drinks_yn = input('\nDrinks? ("yes" or "no") ')
if drinks_yn == 'yes':
    drink_cost = float(input('How much does a drink cost? $'))
    num_drinks = float(input('How many drinks? '))
    drink_total = drink_cost * num_drinks

tax_rate = float(input('\nWhat is the sales tax rate? %'))
tip_percent = float(input('How much would you like to tip? %'))

# Calculations
subtotal = (kids_meal * num_kids) + (adult_meal * num_adults) + drink_total
print(f'\nSubtotal: ${subtotal:.2f}')

sales_tax = subtotal * (tax_rate / 100)
print(f'Sales Tax: ${sales_tax:.2f}')

tip_amount = subtotal * (tip_percent / 100)
print(f'Tip: ${tip_amount:.2f}')

donation = 0
donation_yn = input('\nWould you like to make a donation to Caribou Charities? ("yes" or "no") ')
if donation_yn == 'yes':
    donation = float(input('How much would you like to donate? ($1, $2, $5, $10) $'))

total = subtotal + sales_tax + tip_amount + donation
print(f'Total: ${total:.2f}')

pmt_method = input('\nWhat is your payment method? ("cash" or "card") ')
if pmt_method == 'cash':
    pmt_amt = float(input('\nWhat is the payment amount? $'))
    change = pmt_amt - total
    print(f'Change: ${change:.2f}')
elif pmt_method == 'card':
    cashback = input('Would you like cash back? ("yes" or "no") ')
    if cashback == 'yes':
        cashback_amt = float(input('How much? ($10, $20, $50, $100) $'))

from datetime import date

receipt_yn = input('\nWould you like to print a receipt? ("yes" or "no") ')
if receipt_yn == 'yes':
    print(f'\n------------------------------------\nAndy\'s Burgers\n{date.today()}\nCashier: Bob\n')
    print(f'Kids\' Meal ({num_kids:.0f}@{kids_meal:.2f}ea) ------ ${(num_kids * kids_meal):.2f}')
    print(f'Adult Meal ({num_adults:.0f}@{adult_meal:.2f}ea) ------ ${(num_adults * adult_meal):.2f}')
    print(f'Drinks ({num_drinks:.0f}@{drink_cost:.2f}ea) ---------- ${(num_drinks * drink_cost):.2f}')
    print(f'\n------------------ SUBTOTAL: ${subtotal:.2f}\n')
    print(f'Tax Rate: {tax_rate}% ------------- ${sales_tax:.2f}')
    print(f'Tip: {tip_percent}% ----------------- ${tip_amount:.2f}')
    if donation > 0:
        print(f'Charitable Donation: ------- ${donation:.2f}')
    print(f'\n--------------------- TOTAL: ${total:.2f}\n')
    if pmt_method == 'cash':
        print(f'Received: ------------------ ${pmt_amt:.2f}')
        print(f'Change: -------------------- ${change:.2f}')
    if pmt_method == 'card':
        print('-Payment with card-')
        if cashback == 'yes':
            print(f'Cashback: ----------------- ${cashback_amt:.02f}')
            print(f'Total Payment: ------------ ${(total + cashback_amt):.2f}')
    print('\nThank you for choosing Andy\'s!\nHave a wonderful day!\n------------------------------------\n')
else:
    print('\nThank you for choosing Andy\'s! Have a wonderful day!\n')