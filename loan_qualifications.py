print('\nPlease answer the following questions regarding your loan on a scale of 1 to 10:\n')

loan_size_rating = float(input('How large is the loan? '))
credit_score_rating = float(input('How good is your credit history? '))
income_rating = float(input('How high is your income? '))
down_pmt_size_rating = float(input('How large is your down payment? '))

is_approved = None

if loan_size_rating >= 5:
    if credit_score_rating >= 7 and income_rating >= 7:
        is_approved = True
    elif (credit_score_rating >= 7 or income_rating >= 7) and down_pmt_size_rating >= 5:
        is_approved = True
    else:
        is_approved = False
elif credit_score_rating < 4:
    is_approved = False
elif (income_rating >= 7 or down_pmt_size_rating >= 7) or (income_rating >= 4 and down_pmt_size_rating >= 4):
    is_approved = True
else:
    is_approved = False

if is_approved:
    print('\nYour loan has been accepted.\n')
else:
    print('\nWe\'re sorry, but your loan has been denied.\n')