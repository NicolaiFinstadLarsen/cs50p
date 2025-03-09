import re


def main():
    user_input = input()

    # Walross := to both assign and check boolian
    # _ because i dont use variable again
    if _ := validate(user_input):
        print("True")
    else:
        print("False")


def validate(ip):
    '''
    Since the regex is long, the re.VERBOSE flag can be used.
    To use that I need """ in the front and back
    https://docs.python.org/3/library/re.html#re.VERBOSE

    I have no idea if this is the best way.
    What i have done is map every number with "or" statement
    Numbers are:
    1 or 10-99 or 100-199 or 200-249 or 250-255 and .
    '''

    adress = re.search(
        r"""
    ^([0-9] | ([1-9][0-9]) | (1[0-9]{2}) | (2[0-4][0-9]) | (25[0-5]))\.
    ([0-9] | ([1-9][0-9]) | (1[0-9]{2}) | (2[0-4][0-9]) | (25[0-5]))\.
    ([0-9] | ([1-9][0-9]) | (1[0-9]{2}) | (2[0-4][0-9]) | (25[0-5]))\.
    ([0-9] | ([1-9][0-9]) | (1[0-9]{2}) | (2[0-4][0-9]) | (25[0-5]))$""",
        ip, re.VERBOSE)
    if adress:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
