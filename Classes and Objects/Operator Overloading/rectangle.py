class Rectangle:
    """Represents a rectangle on the coordinate plane.
    Attributes:
        x (int): location x of the rectangle
        y (int): location y of the rectangle
        width (int): width of the rectangle
        height (int): height of the rectangle
    """

    def __init__(self, x=0, y=0, w=1, h=1):
        """Sets teh rectangle's x, y, width, height."""
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def translate(self, dx, dy):
        """Shifts the rectangle's location by dx, dy"""
        self.x += dx
        self.y += dy

    def __str__(self):
        """Returns the rectangle as a string"""
        return "Loc=(" + str(self.x) + "," + str(self.y) + ")" + " W=" + str(self.width) + " H=" + str(self.height)
    
    """
    Overloading operators in the Rectangle
    """
    
    def __add__(self, other):
        """Returns a new rectangle with the dimensions from the two specified rectangles added together."""
        return Rectangle(0, 0, self.width + other.width, self.height + other.height)

    def __eq__(self, other):
        """Compares the two rectangles x, y, width, and height to see if they are equal."""
        return self.x == other.x and self.y == other.y and self.width == other.width and self.height == other.height