# creat a deep function
def deep():
    #ask the users for input
    mesg = input("the answer to the Great Question of Life, the Universe and Everything?  ")
    # call a function call is_even to print YES & NO
    if is_even(mesg):
        print("Yes")
    else:
        print("No")
# creat the function is_even to check the user input
def is_even(mesg):
    if mesg.strip()  == "42" or  mesg.lower().strip() == "forty-two" or mesg.lower().strip() == "forty two" :
        return True
    else:
        return False

deep()
