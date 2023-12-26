
# creat fruits dic
fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plum": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
}

# I ask the user to put name of fruits
ask = input("Item: ")
# lower case
ask_ = ask.lower()
# check and  give us the key
if ask_ in fruits:
    print("calories: ", fruits[ask_])
