import random
import sys
import pyfiglet


if len(sys.argv) == 1:
    f = pyfiglet.figlet_format(input("Input: "), font=random.choice(pyfiglet.FigletFont.getFonts()))
    print(f)
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] not in pyfiglet.FigletFont.getFonts():
            sys.exit("Invalid Usage")
        else:
            f = pyfiglet.figlet_format(input("Input: "), font=sys.argv[2])
            print(f)
    else:
        sys.exit("Invalid Usage")
else:
    sys.exit("Invalid Usage")

# i had to use print(dir(pyfiglet.FigletFont)) and help(pyfiglet.FigletFont.isValidFont) to get oriented
# if len(sys.argv)
