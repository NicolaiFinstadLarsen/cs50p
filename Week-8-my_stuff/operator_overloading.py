class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} galleons,  {self.sickles} sickles, {self.knuts} knuts"
    
    def __add__(self, other): # This is operator overloading.
        # Self is left side of assignment
        # Other is right side of assignment
        # in the line total = harry + ron
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)

harry = Vault(100, 50, 25)
ron = Vault(25, 50, 100)
total = harry + ron
print(harry)
print(ron)
print(total)