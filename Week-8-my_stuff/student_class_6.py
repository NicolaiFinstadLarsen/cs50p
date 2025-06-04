import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(f"{name} is in {house}")


# hat = Hat() trenger ikke denne lenger da jeg bruker @classmethod og cls 
Hat.sort("Harry") # Husk å bruke stor bokstav som tilsvarer class 
Hat.sort("Hermine")
Hat.sort("Ron")