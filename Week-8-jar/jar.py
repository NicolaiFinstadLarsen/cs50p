class Jar:
    def __init__(self, capacity=12):
        self._size = 0
        self._capacity = capacity
        if self._capacity < 0:
            raise ValueError


    def __str__(self):
        return f"{self._size * '🍪'}"


    def deposit(self, n):
        if self._size + n > self.capacity:
            raise ValueError
        self._size += n # no need to return, just update state.
        

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError
        self._size -= n


    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size

jar = Jar(10)
print(jar.capacity)

jar.deposit(3)
print(jar.size)
print(jar)

jar.withdraw(1)
print(jar.size)
print(jar)
