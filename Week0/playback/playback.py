#creat my own function
def ask():
    # Ask the users
    mesg = input("Ask me somting:" )
    # replacing each space with 3 dote
    new_mesg =mesg.replace(" ","...")
    #print the input
    print(new_mesg)
    
ask()
