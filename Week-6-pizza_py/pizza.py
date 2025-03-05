from tabulate import tabulate
import csv
import sys


def main():
    # Exit messages as per problem spec's
    # Taken from lines.py Week-6
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    try:
        file_name = sys.argv[1]
        table = make_table(file_name)
        print(table)
    except FileNotFoundError:
        sys.exit("No such file")


def make_table(file_name):
    dict_list = []
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            dict_list.append(row)

    # print(long)
    return (tabulate(dict_list, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
