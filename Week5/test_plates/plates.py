def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    s = str(s)

    validated = ""
    numcheck = 0

    illegal_symbols = [
        " ",
        ".",
        "?",
        "!",
        ",",
        ":",
        ";",
        "(",
        ")",
        "[",
        "]",
        "'",
        "-",
        '"',
        "/",
        "\\",
        "`",
        "@",
        "#",
        "*",
    ]

    if len(s) >= 2 and len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            for ch in s:
                if ch not in illegal_symbols:
                    if ch.isnumeric() and numcheck == 0 and ch != "0":
                        numcheck += 1
                        validated += ch
                    elif ch.isnumeric() and numcheck > 0:
                        numcheck += 1
                        validated += ch
                    elif ch.isalpha() and numcheck < 1:
                        validated += ch
    else:
        return False

    if validated == s:
        return True
    else:
        return False

if __name__ == "__main__":
    main()