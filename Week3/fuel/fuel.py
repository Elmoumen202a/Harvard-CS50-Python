while True:
# user input
    fuel = input("Fraction:" )
    try:
        # find function ("/")
        i = fuel.find("/")
        a = int(fuel[:i])
        b = int(fuel[i+1:])
        #Calculate
        f = int(a) / int(b)
        if f <= 1 :
            break
    except (ValueError, ZeroDivisionError):
        pass
# precentage by 100
per = int(f * 100)
# Check
if  per <= 1 :
    print("E")
elif per >= 99:
    print("F")
elif per == 66:
    print("67%")
else:
    print(str(per) + "%")
    #print(f"{per}%")
