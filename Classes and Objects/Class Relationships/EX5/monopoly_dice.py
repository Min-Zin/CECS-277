"""
This example program will be a dice roller for the dice game Monopoly.
A Monopoly roller will have a set of two 6-sided dice that can be rolled
and displayed. When the dice are displayed it should show their values in
sorted order, their sum, and whether doubles were thrown. An individual
die can be rolled, compared, summed, and displayed.
"""

import die

class MonopolyDice:
    def __init__(self):
        self.dice = [die.Die(), die.Die()]
    
    def roll_dice(self):
        for d in self.dice:
            d.roll()
        
    def __str__(self):
        s = ""
        self.dice.sort()
        for i, d in enumerate(self.dice):
            s += "D" + str(i+1) + ": " + str(d) + " "
        
        s += "Sum=" + str(self.dice[0] + self.dice [1])

        if self. dice[0] == self.dice[1]:
            s += " You threw doubles!"

        return s
    
    