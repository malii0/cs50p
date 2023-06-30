amount_due = 50
print("Amount Due: "+str(amount_due))

insert_coin = 0

while amount_due - insert_coin >= 0 and amount_due != 0:

    insert_coin = int(input("Insert Coin: "))

    if insert_coin == 5:
        amount_due -= 5

    if insert_coin == 10:
        amount_due -= 10

    if insert_coin == 25:
        amount_due -= 25

    if amount_due > 0:
        print("Amount Due: "+str(amount_due))
    else:
        change_owed = -(amount_due)
        print("Change Owed: "+ str(change_owed))