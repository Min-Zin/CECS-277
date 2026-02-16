class Person:
    """Represents a person.
    Attributes:
        name (str): name of the person.
        address (str): address of the person.
        birth_year (int): year person was born.
    """
    def __init__(self, name, address, b_year):
        """Initializes the name, address, and birth year of the person."""
        self.name = name
        self.address = address
        self.birth_year = b_year

    def age(self, curr_year):
        """Returns the age of the person given the current year."""
        return curr_year - self.birth_year

    def __str__(self):
        """String representation of a person."""
        return "My name is " + self.name + " and I am " + str(self.age(2023)) + " years old.\nI live at " + self.address + "."