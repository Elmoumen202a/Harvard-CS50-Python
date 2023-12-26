# creat the main function
def main():
    # ask the users input
    ask = input()
    # convert function
    mesg = convert(ask)
    print(mesg)

# creat a covert function
def convert(new_mesg):
    #replace for happy emoji & sad emoji
    new_mesg1 = new_mesg.replace(":)","🙂")
    new_mesg2 = new_mesg1.replace(":(", "🙁" )
    # return str
    return new_mesg2

main()