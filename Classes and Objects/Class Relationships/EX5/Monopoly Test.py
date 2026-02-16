"""
Play monopoly dice
"""

import monopoly_dice

def main():
    dice = monopoly_dice.MonopolyDice()
    print(dice)

    dice.roll_dice()
    print(dice)

main()