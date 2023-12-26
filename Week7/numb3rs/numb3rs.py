import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        for num in ip.split("."):
            if 255<int(num) or int(num)<0 :
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()