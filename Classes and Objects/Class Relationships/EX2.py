"""
Class Pond has one or more objects of class Duck. 
Ducks are passed into the add_duck method and those references are 
stored in the ducks list.  Ducks can be later removed.  If the Pond
object is destroyed (dries up?), the Ducks can still exist elsewhere.
"""

class Duck:
    def quack(self):
        return "Quack"

class Pond:
    def __init__(self):
        self.ducks = []

    def add_duck(self, duck):
        self.ducks.append(duck)# stores the ducks

    def quack_ducks(self):
        s = ""
        for d in self.ducks:
            s += d.quack()
        return s

    def remove_duck(self, duck):
        self.ducks.remove(duck)