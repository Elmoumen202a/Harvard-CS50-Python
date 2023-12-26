from os import path
import os
from PIL import Image, ImageOps
import sys

def main():
    # check the command line
    checkCommand()
    try :
    # open the image
        image = Image.open(sys.argv[1])
        #  shirt
        shirt = Image.open("shirt.png")
        size = shirt.size
        fit = ImageOps.fit(image, size)
        fit.paste(shirt, shirt)
        # output image
        fit.save(sys.argv[2])
    # check the file exist
    except FileNotFoundError :
        sys.exit("Input does not exist")

#function check command line
def checkCommand():
    # check
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    firstFile = os.path.splitext(sys.argv[1])
    secondFile = os.path.splitext(sys.argv[2])
    if firstFile[1] != secondFile[1]:
        sys.exit("Input and output have different extensions")
    #check is file.image
    elif firstFile[1] != ".jpg" and firstFile[1] != ".jpeg" and firstFile[1] != ".png":
        sys.exit("Invalid output")

if __name__ == "__main__" :
    main()