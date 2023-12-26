# emty dic
dictionary = {}
# loop
while True:
    try:
        i = input().lower()
        # check the items in dictionary
        if i in dictionary  :
            #if it is add  + 1 in the cont
            dictionary[i] += 1
        else:
            # else just add it for the first time
            dictionary[i] = 1

    except EOFError:
        # use the sorted()  & keys() function
        for k in sorted(dictionary.keys()):
            print(dictionary[k], k.upper())
        # stop
        break

