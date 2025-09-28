from S1E9 import Character


class Baratheon(Character):
    """Baratheon family member."""

    def die(self):
        self.is_alive = False

    def __str__(self):
        return f"{self.first_name}, Alive: {self.is_alive}"

    def __repr__(self):
        return f"Baratheon({self.first_name}, Alive: {self.is_alive})"


class Lannister(Character):
    """Lannister family member."""

    def die(self):
        self.is_alive = False

    def __str__(self):
        return f"{self.first_name}, Alive: {self.is_alive}"

    def __repr__(self):
        return f"Lannister({self.first_name}, Alive: {self.is_alive})"

    @classmethod
    def create_lannister(cls, names, is_alive=True):
        if isinstance(names, str):
            return cls(names, is_alive)
        else:
            return [cls(name, is_alive) for name in names]
