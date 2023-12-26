def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # use str.isalnum() : Return True if all characters in the string are alphanumeric and there is at least one
    # use str.isalpha() : Return True if all characters in the string are alphabetic and there is at least one character, False otherwise.
    if  s.isalnum() and s[0:2].isalpha() and 6 >= len(s) >=2    :
        for x in s:
            # str.isdigit() : Return True if all characters in the string are digits and there is at least one character, False otherwise.
            if x.isdigit():
                clue = s.index(x)
                if s[clue:].isdigit() and int(x) != 0:
                    return True
                else:
                    return False
        return True


main()