cart_items = []
cart_prices = []

def add_item():
    item_to_buy = input('\nWhat would you like to buy? ').title()
    item_price = float(input('How much does it cost? $'))
    cart_items.append(item_to_buy)
    cart_prices.append(item_price)
    print(f'\'{item_to_buy}\' (Item #{len(cart_items)}) added to cart.')

def remove_item():
    item_to_remove = int(input('\nWhich item would you like to remove? Enter the item number: '))
    removed_item = cart_items[item_to_remove-1]
    cart_items[item_to_remove-1] = False
    cart_prices[item_to_remove-1] = 0
    print(f'\'{removed_item}\' removed from cart.')
    # I could have popped these out of the lists, but I wanted to preserve each item's original index.
    # You'll see later on that my code is set to pass over these 'ghost' items.


print('\nWelcome to Wallymart!')
action = ''
while action != 'proceed':
    action = input('\nWould you like to ADD an item, REMOVE an item, or REVIEW your cart? ').lower()
    
    if action == 'add':
        add_item()
    
    elif action == 'remove':
        remove_item()
    
    elif action == 'review':
        print('\nItems in your cart:')
        sum_prices = 0

        for i in range(len(cart_items)):
            if cart_items[i]:
                print(f'- {cart_items[i]}, ${cart_prices[i]:.2f} (Item #{i+1})')
                sum_prices += cart_prices[i]
        
        print(f'Total: {sum_prices:.2f}')
        action = input('\nWould you like to go BACK or PROCEED to checkout? ').lower()

has_discount = input('\nDo you have a discount code? (yes/no) ').lower()
if has_discount == 'yes':
    discount_code = input('Enter discount code: ')
    discount_amount = 5 * (len(discount_code) - 1)
    print(f'Your discount: ${discount_amount:.2f}')

print('\nYou are purchasing: ')
item_count = 0
for item in cart_items:
    if item:
        print(item)
        item_count += 1
days_to_ship = round(item_count / 2)

sum_prices = 0
for item in cart_prices:
    sum_prices += item
with_discount = sum_prices - discount_amount
if with_discount < 0:
    with_discount = 0

print(f'For a total of ${with_discount:.2f}. Your order will arrive in {days_to_ship} days.')

print('\nThank you for your purchase! Come again soon!\n')