"""
Main program to test the Die class
"""

import die

def display_dice(d1, d2):
    if d1 < d2:
        print("D1 =", d1)
        print("D2 =", d2)
    else:
        print("D1 =", d2)
        print("D2 =", d1)
        if d1 == d2:
            print("You got doubles!")
    print("Sum =", d1 + d2)

def main():
    dice1 = die.Die()
    dice2 = die.Die()
    display_dice(dice1, dice2)
    print()
    dice1.roll()
    dice2.roll()
    display_dice(dice1, dice2)

main()