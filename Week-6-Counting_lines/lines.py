import sys

def main():
    # Exit messages as per problem spec's
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


'''
Reading lines in a .py file 
and not counting comment # lines or whitespacelines
'''

def read(name):
    counter = 0
    with open(name, "r") as file:
        rows = file.readlines() # readlines and not readline.

        for row in rows:
            row = row.lstrip() 
            # Since row.strip() == True is there is text left after strip \n
            # not row.strip to get a False if the row has text. \n
            # To not skip valid code lines.  
            if row.startswith("#") or not row.strip():  # not row.strip to get a true of the row is not empty. 
                continue
            else:
                # print(row)
                counter += 1
    return counter

if __name__ == "__main__":
    main()

    