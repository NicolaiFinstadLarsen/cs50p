import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    '''
    \b	Returns a match where the specified characters are at the beginning or at the end of a word
    (the "r" in the beginning is making sure that the string is being treated as a "raw string")
    '''
    full_list = re.findall(r"\bum\b", s, re.IGNORECASE)
    print(full_list)
    return len(full_list)



if __name__ == "__main__":
    main()