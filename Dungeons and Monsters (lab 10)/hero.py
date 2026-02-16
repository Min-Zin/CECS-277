from entity import Entity
import random

class Hero(Entity):
    def __init__(self, name):
        super().__init__(name, 25)
        self.row = 0
        self.col = 0
    
    def attack(self, entity):
        # Random damage in the range 2~5
        dmg = random.randint(2,5)
        entity.take_damage(dmg)
        # Return the string of what happened
        return f'You attack {entity} and dealt {dmg} damage.'
    
    """
    Movements:
        Only if location is within the bounds of map (0 and len(map)-1)
        If not return a 'o' to signify that direction is out of bound
    """

    def go_north(self, dungeon_map):
        # Update the hero's location by subtracting 1 to row
        if self.row > 0:
            self.row -= 1
            return dungeon_map[self.row][self.col]
        return 'o'

    def go_south(self, dungeon_map):
        # Update the hero's location by adding 1 to row
        if self.row < len(dungeon_map) -1:
            self.row += 1
            return dungeon_map[self.row][self.col]
        return 'o'

    def go_east(self, dungeon_map):
        # Update the hero's location by adding 1 to column
        if self.col < len(dungeon_map[0]) -1:
            self.col += 1
            return dungeon_map[self.row][self.col]
        return 'o'

    def go_west(self, dungeon_map):
        # Update the hero's location by subtracting 1 to column
        if self.col > 0:
            self.col -= 1
            return dungeon_map[self.row][self.col]
        return 'o'