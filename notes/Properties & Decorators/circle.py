class Circle:
    """Represents a circle with a radius.
    Attributes:
        radius(int) - radius of the circle.
    """
    def __init__(self, radius):
        """Initializes the radius of the circle."""
        self.radius = radius

    def get_radius(self):
        """Retruns the circle's radius"""
        return self.radius
    
    def set_radius(self, radius):
        """Update the circle's radius"""
        if type(radius) == int:
            if radius > 0:
                self._radius = radius
            else:
                raise ValueError("Radius must be positive.")
        else:
            raise TypeError("Radius must be a number.")
        
    def calc_area(self):
        """Calculates the area of the circle."""
        return 3.14 * self.radius * self.radius

    def calc_circumference(self):
        """Calculates the circumference of the circle."""
        return 2 * 3.14 * self.radius

    def __str__(self):
        """Represents the circle as a string."""
        return "Radius = " + str(self.radius)

