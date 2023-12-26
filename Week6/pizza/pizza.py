from tabulate import tabulate
import csv
import sys

def main():
    # check the command line
    checkCommand()
    try :
    # open the file
        with open(sys.argv[1], "r") as csvf :
            # creat emty table
            table = []
            for row in csv.reader(csvf):
                table.append(row)
    # check the file exist
    except FileNotFoundError :
        sys.exit("File does not exist")
    #  the table
    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))

#function check command mline
def checkCommand():
    # calculate how the command line in file.CSV
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    # check is file.CSV
    elif sys.argv[1].endswith('.csv') != True:
        sys.exit("Not a csv file")

if __name__ == "__main__" :
    main()