import re

def main():
    print(count(input("Text: ")))

def count(s):
    return len(re.findall(r"\b\W*(um)|(Um)|('...')\W", s))

if __name__ == "__main__":
    main()