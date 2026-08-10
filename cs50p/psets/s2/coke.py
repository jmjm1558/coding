amount_due = 50
balance = 0
allowed_coins = [25, 10, 5]
while True:
    print("Amount Due:", amount_due)
    x = int(input("Insert Coin: "))
    if x in allowed_coins:
        amount_due -= x
    else:
        continue
    if amount_due == 0:
        print("Change Owed:", amount_due)
        break
    elif amount_due < 0:
        print("Change Owed:", abs(amount_due))
        break


