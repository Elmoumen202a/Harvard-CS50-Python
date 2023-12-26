name = input("camelCase: " )
print("snake_case: ", end="")
# loop
for x in name:
    # check upper case
    if x.isupper():
        print("_"+ x.lower(), end="")
    else:
        print(x, end="")
#print sapce in end
print()

