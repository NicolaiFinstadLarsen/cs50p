from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

def main():

    # To check for errors in command line input
    argv_check = ["-f", "--f"]
    all_fonts = figlet.getFonts()

    if len(sys.argv) > 3 or len(sys.argv) == 2:
        sys.exit("Unsafe use")
        

    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font)
        print(f"Font chosen by random.choice is: {font}, how delightfull")

    elif len(sys.argv) == 2 and sys.argv[1] not in argv_check:
        sys.exit("Unsafe again")

    elif len(sys.argv) == 3 and sys.argv[2] not in all_fonts:
             sys.exit("Unsafe a third time")

    else:
        if len(sys.argv) == 3 and sys.argv[1] in argv_check:
            font = sys.argv[2]
            figlet.setFont(font=font)


    if font not in all_fonts:
        sys.exit("No font in fonts")
    
    text = input("Text: ")

    print(figlet.renderText(text))
    


main()