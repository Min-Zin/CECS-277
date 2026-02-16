"""a Circle class that needs to be tested.
The TestCircle class extends the TestCase class and
 has test methods for checking the area and circumference methods."""
import unittest

class Circle:
        def __init__(self, radius):
            self.radius = radius

        def calc_area(self):
            return 3.14 * self.radius * self.radius

        def calc_circumference(self):
            return 2 * 3.14 * self.radius

class TestCircle(unittest.TestCase):
        def test_area(self):
            c = Circle(2)
            self.assertEqual(c.calc_area(), 12.56)

        def test_circumference(self):
            c = Circle(3)
            self.assertEqual(c.calc_circumference(), 18.84)

unittest.main(exit=False)