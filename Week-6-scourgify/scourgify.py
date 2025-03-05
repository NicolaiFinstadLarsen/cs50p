import sys
import csv

'''
Usage:

python scourgify.py before.csv my_choice.csv

The program handles the before.csv file and outputs
a new file with commandline arguments as filename.
The new file will have seperated the first and
last name of the names on the list

Keeping in mind that the before file will
have the last name listed first.
The output file should have the first name listed
first.
'''


def main():
    # argv checks
    # if len(sys.argv) < 3:
    #     sys.exit("Too few command-line arguments")
    # if len(sys.argv) > 3:
    #     sys.exit("Too many command-line arguments")
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py before.csv my_choice.csv")
    try:
        temp_out = clean_file(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File not found")

    write_file(temp_out)


def clean_file(file_name):
    full_csv_list = []

    counter = 0
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        # Apperantly there is a
        # next(reader)
        # to skip the header
        for row in reader:
            # Then all of the is better in the
            # write_file func as just to add
            # the header like:
            # writer.writerow("first", "last", "house")
            if counter == 0:
                headers = ["first", "last", "house"]
                counter += 1
                continue
            # Splitting to get two variables i can add back later
            last_name, first_name = row[0].split(", ")

            # New list, appending everything and
            # appending that list to the main list.
            new_row = []
            new_row.append(first_name)
            new_row.append(last_name)
            new_row.append(row[1])

            full_csv_list.append(new_row)
        # Inserting headers to first index of list,
        # since i need them for the write part.
        full_csv_list.insert(0, headers)
        return full_csv_list


def write_file(temp):
    # Write since i handle the whole file each time.
    with open(sys.argv[2], "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(temp)


if __name__ == "__main__":
    main()
