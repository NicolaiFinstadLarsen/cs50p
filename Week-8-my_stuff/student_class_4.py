class Student:
    def __init__(self, name, house, patronus):
        if not name: 
            raise ValueError("Not working")
        if house not in ["oslo", "bergen", "trondheim"]:
            raise ValueError("Not a city")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "stag":
                return "😄"
            case "otter":
                return "🦦"
            case "jack russel terrier":
                return "🐶"
            case _:
                return "🪄"


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input("Name: ").lower()
    house = input("House: ").lower()
    patronus = input("Patronus: ").lower()
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()