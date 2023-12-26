# users inout
mesg = input("Greeting: ")
# use lower() & strip()
x = mesg.lower().strip()
# write if statment to check the user's input
if "hello" in x:
    print("$0")
elif "h" == x[0]:
    print("$20")
else:
    print("$100")




