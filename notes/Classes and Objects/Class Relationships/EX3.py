"""
Class House has created several Room objects that are stored 
in the rooms list.  The House object owns those Room objects, 
the references are not stored anywhere else.  If the house is
destroyed, then all the rooms are destroyed along with it.
"""

class Room:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class House:
    def __init__(self):
        self.rooms = [Room("Kitchen"), Room("Bedroom"), Room("Bathroom"), Room("Living Room")]

    def __str__(self):
        s += ""
        for r in self.rooms:
            s += str(r)
        return s