def main():
    string = input("What is the Great Question of Life, the Universe and Everything: ").strip()

    if answer(string):
        print("Yes")
    else:
        print("No")


def answer(s):
    if s.isdigit() and s == "42":
        return True
    elif s.lower() == "forty-two" or s.lower() == "forty two":
        return True
    else:
        return False


main()
