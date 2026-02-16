class Item:
    """Represents a restaurant menu item.
    Attributes:
        name (str) - name of item
        price (int) - price of item
        cookable (bool) - if item is cookable
    """
    def __init__(self, name, price, cookable):
        """Initializes the item with a name, price, and cookability."""
        self._name = name
        self._price = price
        self._cookable = cookable

    @property
    def name(self):
        """Returns the name of the item."""
        return self._name

    @property
    def price(self):
        """Returns the price of the item."""
        return self._price

    def __str__(self):
        """Returns the string representation of the item."""
        return self._name + ' $' + str(self._price)

    def is_cookable(self):
        """Returns the cookability of the item."""
        return self._cookable