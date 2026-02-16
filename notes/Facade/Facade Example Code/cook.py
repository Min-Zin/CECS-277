class Cook:
    """Represents a restaurant cook.
    Attributes:
        cookable_items (Item []) - list of items to cook.
    """
    def __init__(self):
        """Initializes the list of items the cook will make."""
        self._cookable_items = []

    def add_cookable_item(self, item):
        """Adds an item to the cook's list."""
        self._cookable_items.append(item)

    def make_item(self, item):
        """Cook makes and removes an item from the list."""
        self._cookable_items.remove(item)
        return "Finished making a "+ item.name