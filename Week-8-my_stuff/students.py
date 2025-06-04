def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw" # Changing student house
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house] # Returns a list, not a tuple. Since tuple is inmuteable. List is muteable.


if __name__ == "__main__":
    main()