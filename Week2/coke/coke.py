# variable
amount_due = len(range(50))
# (wile) loop  amount_due is true
while amount_due > 0:
    print ("Amount Due:", amount_due)
    # the users input
    insert_coin = int(input("Isert Coin: "))

    if insert_coin in [5,10,25]:
        amount_due -= insert_coin  # amount_due = amount_due - insert_coin

#calculate change
change = abs(amount_due)
# result
print("Change owed: ", change)

