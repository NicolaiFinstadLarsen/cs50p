import string

"""
TODO
OK -“All vanity plates must start with at least two letters.”
OK -“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
-“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
OK -“No periods, spaces, or punctuation marks are allowed.”
"""


def main():
    # plate = "cs50p2"
    # plate = "ECTO88"
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # Check length is good and keep rest of code inn this scope.
    # print(plate[2])
    if len(list(plate)) > 2 and len(list(plate)) <= 6:
        for c in plate[0:2]:
            # print(c)
            if c.isalpha() == False:
                # print("False 1")
                return False

        # TODO Check if there is an int in plate of it ends in alpha.
        if plate[-1].isalpha():
            if plate[2:-1].isdecimal():
                # print("False 2")
                return False

        # TODO Check if last char is an digit/int, if true; there can not be digit before last alpha.
        # Check if last char is a decimal
        if plate[-1].isdigit():
            # Check if where the last alpha char is in string
            for c in plate[2:-1]:
                if c.isalpha():
                    # Store index of last alpha char
                    x = plate.find(c)
                    # print(plate)
                    # print(x)
                    # print(f" This is a print for plate[2:x+1] -> {plate[2:x+1]}")

                    # Checking if there is any digit before last alpha char
                    for c in plate[2:x+1:]:
                        # print(f" This is a line 53 print for c -> {c} in plate[2:x+1] -> {plate[2:x+1]}")
                        if c.isdigit():
                            # print(f" Pos of x = {x} and c is {c}")
                            # print("False 3")
                            return False

        # TODO The first number used cannot be a ‘0’.”
        if plate[2] == "0":
            # print("False 4")
            return False

        # TODO Check if there is any punctuation mark etc
        for c in plate:
            if c in string.punctuation:
                # print("False 5")
                return False

        # print("True 2")
        return True

    else:
        # print("False 6")
        return False


main()
