import circle

def main():
    c1 = circle.Circle(2)
    print(c1)                      # Radius = 2
    c1.radius = -2
    print(c1.calc_circumference()) # -12.56
    c1.radius = "A"
    print(c1.calc_area())          # TypeError

main()