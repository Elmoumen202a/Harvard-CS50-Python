#Prompts the user for a level n, . If the user does not input a positive integer, the program should prompt again.
#Randomly generates an integer between 1 and n , inclusive, using the random module.
#Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
#If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
#If the guess is larger than that integer, the program should output Too large! and prompt the user again.
#If the guess is the same as that integer, the program should output Just right! and exit.

import random

while True:
    try:
        input_level = int(input("Level: "))
        # level
        if  input_level > 0 :
            break
    except :
        pass
# random number
chooce_number_in = random.randint(1, input_level)
# guess
while True:
    try:
        input_guess = int(input("Guess: "))
        if  input_guess > 0  :
            # check
            if input_guess > chooce_number_in :
                print("Too large!")
            elif input_guess < chooce_number_in:
                print("Too small!")
            elif input_guess == chooce_number_in:
                print("Just right!")
                break
            else:
                continue
    except:
        pass
