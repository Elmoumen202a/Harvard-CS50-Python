vowels = ["a", "e", "i", "o", "u"]

def main():
    word = str(input("Input: ").strip())
    print(f"Output: {shorten(word)}")

def shorten(word):
    new_string = ""
    for letter in word:
        if letter.lower() not in vowels:
            new_string += letter

    return new_string

if __name__ == "__main__":
    main()