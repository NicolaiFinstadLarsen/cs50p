class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod # Vi kan kalle methoden på klassen og ikke objektet
    # Classmoethods tar normalt cls. Dette gjør at vi kan jobbe på selve klassen eller nye instancer.
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get() # Vi flytter logikken for å opprette en Student fra main til Student-klassen.

    print(student)


if __name__ == "__main__":
    main()