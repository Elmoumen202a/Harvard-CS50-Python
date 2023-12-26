from validator_collection import validators, checkers, errors

def main():
    # user input
    email_address = input("What's your email address: ")
    # check
    is_email_address = checkers.is_email(email_address)
    if is_email_address == True:
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()