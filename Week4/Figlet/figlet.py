# inpurt modules
from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
# n = number of list(sys.argv)/ r = random of fonts
n = len(sys.argv)
r = random.choice(figlet.getFonts())
# Zero if the user would like to output text in a random font.
#if the user would like to output text in a specific font,
# in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
if n<2 :
    figlet.setFont(font = r)
elif n >=2 and sys.argv[1] == "-f":
    figlet.setFont(font = sys.argv[2])

elif n>3 or n<1 or sys.argv[1] != "-f":
    sys.exit("Invalid Usage")



inp = input("Input: ")
print("Otput: ")
print(figlet.renderText(inp))