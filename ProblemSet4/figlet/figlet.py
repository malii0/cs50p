from pyfiglet import Figlet
import sys


if sys.argv[1] not in ["-f", "-font"]:
    sys.exit("Invalid usage")

input = input("Input: ")

figlet = Figlet()
figlet.getFonts()

figlet.setFont(font = sys.argv[2])

print(figlet.renderText(input))