class Jar:
    def __init__(self, capacity=12):
        if self.capacity < 0:
            raise ValueError
        self.total = 0
        self.capacity = capacity


    def __str__(self):
        return f"{self.total * '🍪'}"

    def deposit(self, n):
        if self.total + n > self.capacity:
            raise ValueError
        self.total += n # no need to return, just update state.
        

    def withdraw(self, n):
        if self.total - n < 0:
            raise ValueError
        self.total -= n

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...