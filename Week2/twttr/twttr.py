
input_ = input("Input:" )
output = print("Outout:",end="" )
vowels = ["u","e","i","a","o"]
#loop in evry letter
for l in input_:
    if not l.lower() in vowels:
        print(l, end="")
# new line
print()

