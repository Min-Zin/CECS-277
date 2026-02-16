import circle2

def main():
    c1 = circle2.Circle(2)
    print(c1)             # Radius = 2
    c1.radius = "A"       # Radius must be a number.
    c1.radius = 4
    print(c1)             # Radius = 4
    print(c1.calc_area()) # 50.24
    c1._radius = "A"      # can still modify attribute

main()