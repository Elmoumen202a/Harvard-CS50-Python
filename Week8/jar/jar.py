class Jar:
    def __init__(self, capacity=12):
        if 0 > capacity :
            raise  ValueError
        self.capacity_ = capacity
        self.size_ = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n> self.capacity or self.size + n > self.capacity:
            raise ValueError
        self.size_ += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError
        self.size_ -= n

    @property
    def capacity(self):
        return self.capacity_

    @property
    def size(self):
        return self.size_

