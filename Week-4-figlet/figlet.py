from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

def main():

    argv_check = ["-f", "--f"]
    #print(len(sys.argv))

    all_fonts = figlet.getFonts()

    if len(sys.argv) > 3 or len(sys.argv) == 2:
        # print(f"length = {len(sys.argv)}")
        # print("Error")
        sys.exit("Unsafe use")

    elif len(sys.argv) > 1 and sys.argv[1] not in argv_check:
        sys.exit("Unsafe again")

    elif len(sys.argv) > 2 and sys.argv[2] not in all_fonts:
             sys.exit("Unsafe a third time")

    text = input("Text: ")

    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
        #print(font)
        figlet.setFont(font=font)

    else:
        if len(sys.argv) == 3 and sys.argv[1] in argv_check:
            font = sys.argv[2]
            figlet.setFont(font=font)

    # Siste exit som må flytte til før prompt av text
    if font not in all_fonts:
        sys.exit("No font in fonts")

    print(figlet.renderText(text))
    


main()