class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod # På denne måten initializer vi Student objektet i student class'en internt.
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get() # På denne måten fjerner vi studentlogikken fra main til Student class
    print(student)

if __name__ == "__main__":
    main()