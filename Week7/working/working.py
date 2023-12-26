import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    try:
        # check error
        if "-" in s:
            raise ValueError

        s = s.split(" to ")
        listForTime = []

        for x in s:
            # check time
            time = re.search("\d+:\d+",x)

            if time:
                # check time
                check = time[0].split(":")
                digit = int(check[0])
                #PM
                if "PM" in x.split(" "):
                    if check[0] == "12":
                        listForTime.append(f"12:{check[1]}")
                    else:
                        convertAll = int(check[0]) + 12
                        listForTime.append(f"{str(convertAll):02}:{check[1]}")
                #AM
                if "AM" in x.split(" "):
                    if digit == 12:
                        listForTime.append(f"00:{check[1]}")
                    else:
                        listForTime.append(f"{digit:02}:{check[1]}")
                # check error
                if int(check[0]) >= 13 or int(check[1]) > 59:
                    raise ValueError

            else:
            # digit
                digit = x.split(" ")
                #PM
                if "PM" in digit[1]:
                    if int(digit[0]) == 12:
                        listForTime.append(f"12:00")
                    else:
                        convertAll = int(digit[0]) + 12
                        listForTime.append(f"{str(convertAll):02}:00")
                #AM
                if "AM" in digit[1]:
                    if int(digit[0]) == 12:
                        listForTime.append(f"00:00")
                    else:
                        listForTime.append(f"{int(digit[0]):02}:00")

        return " to ".join(listForTime)

    except:
        raise ValueError

if __name__ == "__main__":
    main()