import sys
import csv
'''
I did not know how to use DictReader and this is a learning cours
so I asked gpt since lecture said column changing is better with dict reader
'''

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py before.csv after.csv")

    try:
        clean_data = clean_file(sys.argv[1])
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    write_file(clean_data, sys.argv[2])

def clean_file(input_filename):
    cleaned_rows = []

    with open(input_filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            last_name, first_name = row["name"].split(", ")
            cleaned_rows.append({"first": first_name, "last": last_name, "house": row["house"]})

    return cleaned_rows

def write_file(data, output_filename):
    with open(output_filename, "w", newline="") as file:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()  # Write column names
        writer.writerows(data)  # Write data

if __name__ == "__main__":
    main()

'''
hy This is Better
✅ More Readable:

csv.DictReader lets us refer to column names (row["name"], row["house"]) instead of using numeric indexes (row[0], row[1]).
csv.DictWriter ensures we don't have to manually track column order.
✅ More Maintainable:

If the CSV structure changes (e.g., column order shifts), this will still work without modifications.
✅ Handles Headers Automatically:

No need for next(reader), since DictReader automatically skips headers.
✅ Scales Well:

If more columns are added in the future, they can be handled without changing index numbers.
'''
