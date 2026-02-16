import Point

def movePoint(pt):
    """ Shifts and displays the updated point."""
    pt.translate(1, 1)
    print(pt)

def newPoint():
    """Creates and returns a new point at (3,3)."""
    return Point.Point(3, 3)

def main():
    point4 = newPoint() # (3,3)
    movePoint(point4)    # (4,4)
    print(point4)

main()
