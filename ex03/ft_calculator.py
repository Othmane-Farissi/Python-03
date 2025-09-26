class calculator:
    """Class to apply operations on vectors"""

    def __init__(self, vector):
        self.vector = vector

    def __add__(self, scalar):
        self.vector = [v + scalar for v in self.vector]
        print(self.vector)

    def __mul__(self, scalar):
        self.vector = [v * scalar for v in self.vector]
        print(self.vector)

    def __sub__(self, scalar):
        self.vector = [v - scalar for v in self.vector]
        print(self.vector)

    def __truediv__(self, scalar):
        self.vector = [v / scalar for v in self.vector]
        print(self.vector)
