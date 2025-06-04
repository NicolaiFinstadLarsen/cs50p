class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("No name")
        self.name = name

    ...

    
class Student(Wizard): # Dette gir oss inheritence fra Wizard class
    def __init__(self, name, house):
        super().__init__(name) # Super er foreldre classen og init name \n
        # er for å bruke name fra den klassen
        # self.name = name # Derfor trenger vi ikke denne.
        self.house = house

    ...


class Professor(Wizard): 
    def __init__(self, name, subject):
        super().__init__(name)
        # self.name = name
        self.subject = subject

    def __str__(self):
        return f"{self.name} is teaching {self.subject}"

    ...

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Sverus", "Defense Against The Black Arts")

print(professor)