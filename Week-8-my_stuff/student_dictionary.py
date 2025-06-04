def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw" # Changing student house with dict
    print(f"{student['name']} from {student['house']}") # Remember single and double quotes.
    # Dicts give more clear print statement and we do not need to \n
    # remember the index as with a list or tuple.


def get_student():
    student = {} # Dict is also muteable.
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student 


if __name__ == "__main__":
    main()