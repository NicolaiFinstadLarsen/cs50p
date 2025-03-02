import sys

def main():
    if len(sys.argv) < 2:
        # print("Usage python lines.py 'file to read'")
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    try:
        print(read(sys.argv[1]))
    except FileNotFoundError:
        sys.exit("File does not exist")

def read(name):
    counter = 0
    with open(name, "r") as file:
        rows = file.readlines() # readlines and not readline.

        for row in rows:
            row.lstrip()
            if row.startswith("#") or row.startswith("\n"):
                pass
            else:
                # print(row)
                counter += 1
    return counter

if __name__ == "__main__":
    main()

    