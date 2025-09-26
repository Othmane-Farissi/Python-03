from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    """King family member""" 

    def set_eyes(self, color):
        """Setter for eyes colors"""
        self.eyes = color

    def get_eyes(self):
        """Getter for eyes colors"""
        return self.eyes

    def set_hairs(self, color):
        """Setter for hairs colors"""
        self.hairs = color

    def get_hairs(self):
        """Getter for hairs colors"""
        return self.hairs
