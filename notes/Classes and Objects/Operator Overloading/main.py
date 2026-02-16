import rectangle

def isRectEqual(r1, r2):
    """Displays whether the two rectangles are equal."""
    if r1 == r2:
        print(str(r1) + " is equal to " + str(r2))

    else:
        print(str(r1) + " is not equal to " + str(r2))

def main():
    rect1 = rectangle.Rectangle() # 0, 0, 1, 1
    rect2 = rectangle.Rectangle(1, 2, 3, 4)
    rect3 = rect1 + rect2         # 0, 0, 4, 5
    rect4 = rectangle.Rectangle(0, 0, 4, 5)

    isRectEqual(rect1, rect2) #not equal
    isRectEqual(rect3, rect4) #equal

main()