class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # Getter
    @property
    def name(self):
        return self._name

    # Getter
    @property
    def house(self):
        return self._house
    
    #Setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("No name input")
        self._name = name
    
    # Setter
    # Vi kan ikke nå skrive student.house = "Kristiansand" i koden 
    # student.house kjører denne setter koden
    # Dette er en failsafe for at kode ikke skal endres uten av man ønsker det.
    @house.setter
    def house(self, house):
        if house not in ["oslo", "bergen", "trondheim"]:
            raise ValueError("Invalid House")
        self._house = house


def main():
    student = get_student()
    # student.house = "Kristiansand" # Denne kan ikke lenger brukes.
    # student._house = "Kristiansand" # Denne virker fortsatt da..
    print(student)


def get_student():
    name = input("Name: ").lower()
    house = input("House: ").lower()
    return Student(name, house)


if __name__ == "__main__":
    main()