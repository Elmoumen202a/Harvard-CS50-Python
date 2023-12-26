# menu dictionary :
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
# set amount = 0
amount = 0
#loop
while True:
    try:
        # user input and set it to title case by title() function
        i = input("Item: ").title()
        #check
        if i in menu :
            # culcalate
            amount += menu[i] # amount = amount + menu[ key]
            # 2 decimate places
            amount_ ="{:.2f}".format(amount)
            # print the price
            print(f"Total: ${amount_}")
    except EOFError:
        print()
        break