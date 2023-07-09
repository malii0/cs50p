class Jar:
    def __init__(self, capacity=12):
        if capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError

        self.cookies = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n > self.capacity or n + self.size > self.capacity:
            raise ValueError
        self.cookies += n

    def withdraw(self, n):

        if n <= self.cookies:
            self.cookies -=  n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies