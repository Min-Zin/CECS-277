import circle

def main():
    c1 = circle.Circle(2)
    print(c1)                      # Radius = 2
    c1.radius = -1                 # no effect on _radius
    #c1.set_radius("A")             # Radius is not a number.  TEST 1 by 1
    #c1.set_radius(-3)              # Radius must be positive.
    c1.set_radius(4)
    print(c1.calc_area())          # 50.24
    c1._radius = "A"               # can still modify attribute
    print(c1.calc_circumference()) # TypeError

main()