class Point:
    """ Represents a point on the coordinate plane.
    Attributes:
        x (int): x value of the point
        y (int): y value of the point
    """
    def __init__(self, x=0, y=0):
        """Sets teh x and y values of the point."""
        self.x = x
        self.y = y
    
    def translate(self, dx, dy):
        """Shifts the point by dx and dy."""
        self.x += dx
        self.y += dy

    def __str__(self):
        """Returns the point as a formatted string"""
        return f"X = {str(self.x)} Y = {str(self.y)}"