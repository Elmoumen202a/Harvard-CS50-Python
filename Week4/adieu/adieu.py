# inmport models
import inflect
p = inflect.engine()

mylist = []
while True:

    try:
        inp = input("Name: ")
        mylist.append(inp)
        # usig iflect module
        result = p.join((mylist))
    except EOFError:
        print()
        # output
        print("Adieu, adieu, to " + result )
        # after result break
        break
    else:
        continue




