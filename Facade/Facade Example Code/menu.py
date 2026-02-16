import item

class Menu:
    """Represents the list of menu items at a restaurant.
    Attributes:
        menu (Item []) - list of menu items.
    """
    def __init__(self):
        """Populates the menu from a file."""
        self._menu = []
        file = open("abc.txt") #ex. Fries,2,True
        for i in file:
            vals = i.strip().split(",")
            self._menu.append(item.Item(vals[0], int(vals[1]), vals[2] == "True"))

    def __getitem__(self, i):
        """Returns the item in the list given the index."""
        return self._menu[i]

    def __len__(self):
        """Returns the number of items in the menu."""
        return len(self._menu)

    def get_item_by_name(self, item_name):
        """Searches the menu and returns the matching item."""
        for i in self._menu:
            if item_name == i.name:
                return i