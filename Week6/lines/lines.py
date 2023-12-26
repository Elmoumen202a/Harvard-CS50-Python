import sys

def main():
    # check the command line
    checkCommand()
    # open the file
    try:
        file = open(sys.argv[1], "r")
    # check the file exist
    except FileNotFoundError :
        sys.exit("File does not exist")
    # check uf start wuth # / whitespace
    count = 0
    for ln in file.readlines() :
        if commentORemptyLine(ln) == False :
            count += 1
    print(count)

# function check # and emplty line
def  commentORemptyLine(ln):
    if ln.lstrip().startswith("#")  or  ln.isspace():
        return True
    return False

#function check command mline
def checkCommand():
    # calculate how the command line in file.py
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    # check is file.py
    elif sys.argv[1].split('.')[-1] != "py":
        sys.exit("Not a Python file")


if __name__ == "__main__" :
    main()