class Student:
    def __init__(self, name, house): # This is a method (a function inside a class)
        self.name = name
        self.house = house
        self.house = self.house+" hi" # Changing the object we created


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # contructor call
    student = Student(name, house) # Calling the function (class), passing two values 
    return student


if __name__ == "__main__":
    main()