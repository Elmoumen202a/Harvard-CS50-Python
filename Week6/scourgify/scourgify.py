import csv
import sys

def main():
    # check the command line
    checkCommand()
    lst =[]
    try :
    # open the file
        with open(sys.argv[1], "r") as csvf:
            for row in csv.DictReader(csvf):
                splitWord = row["name"].split(",")
                lst.append(
                    {
                        "firstName": splitWord[1].lstrip(),
                        "secondName" : splitWord[0],
                        "house" : row["house"]
                    }
                )
    # check the file exist
    except FileNotFoundError :
        sys.exit(f"Could not read {sys.argv[1]}")
    #  creat new file.CSV
    with open(sys.argv[2], "w") as csvfile:
        fieldnames = ["firstName","secondName","house"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        #writer.writerow({"firstName":"firstName","secondName": "secondName","house": "house" })
        for row in lst :
            writer.writerow({"firstName":row["firstName"],"secondName": row["secondName"],"house": row["house"]})
#function check command mline
def checkCommand():
    # calculate how the command line in file.CSV
    if len(sys.argv) > 3:
        sys.exit("Too many c-l arguements")
    elif len(sys.argv) < 3:
        sys.exit("Too few c-l arguements")
    #check is file.CSV
    elif sys.argv[2].endswith('.csv') != True or  sys.argv[1].endswith('.csv') != True:
    #elif ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a csv file")

if __name__ == "__main__" :
    main()