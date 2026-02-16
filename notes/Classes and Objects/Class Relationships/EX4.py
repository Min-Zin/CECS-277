"""
Class Dog extends class Animal and gains all the attributes
and methods of Animal.
"""

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def bark(self):
        return self.name + " says 'Woof!'"