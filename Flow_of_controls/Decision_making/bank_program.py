amount = int(input('enter a amount '))
fixed_amount = 100000
balance = fixed_amount-amount
if amount>fixed_amount:
    print('insufficient balance')
else:
    print('your balance is ',balance)
