"""
This is ugly. 
I should not itterate over names every time to check is its == last name.
I should prob not have 4 different print statements..
"""

def main():

    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except (EOFError, KeyboardInterrupt):
            break

    last_name = names[-1]
    if len(names) > 1:
        next_last = names[-2]
    # print(type(last_name))

    print()
    print(f"Adieu, adieu, to",end='')

    if len(names) == 1:
        print(f"Adieu, adieu, to {last_name}")
        return 0

    if len(names) == 2:
        print(f"Adieu, adieu, to {next_last} and {last_name}")
        return 0

    for name in names:
        # print(f"for name: {name}")
        # print(f"Last name: {last_name}")
        if name == str(last_name) and len(names) > 1:
            print(f" and {last_name}")
            return
        print(f" {name},", end='')


main()
