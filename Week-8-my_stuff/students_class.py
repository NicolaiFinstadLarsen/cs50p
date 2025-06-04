class Student: # Making the class
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    student = Student() # Intitialize the object (intstance) student in the class Student
    student.name = input("Name: ") # instance variable
    student.house = input("House: ") # instance variable
    return student # Returns a student to the class Student


if __name__ == "__main__":
    main()