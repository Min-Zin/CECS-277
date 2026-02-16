import random

"""
Class Player has a dependency on class Die.  The Player's turn method passes in a Die object and uses the Die's roll method. 
"""

class Die:
    def roll(self):
        return random.randint(1, 6)
    
class Player:
    def turn(self, die):
        self.val = die.roll() # player has a dependency on Die