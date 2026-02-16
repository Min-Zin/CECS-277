class Cashier:
    """Represents the cashier at a restaurant.
    Attributes:
        order_items (Item []) - list of items in the order.
        cook (Cook) - the restaurant cook
    """
    def __init__(self, cook):
        """Initializes the list of order items and the cook."""
        self._order_items = []
        self._cook = cook

    def add_item(self, item):
        """Adds an item to the order."""
        self._order_items.append(item)

    def calc_total(self):
        """Returns the total cost of the order."""
        total = 0
        for item in self._order_items:
            total += item.price
        return total

    def get_non_cookable_item(self, item):
        """Cashier grabs the non-cookable item."""
        return "Getting " + item.name   

    def bag_order(self):
        """Cashier gathers the ordered items together."""
        s = ""
        for item in self._order_items:
            if item.is_cookable():
                s += self._cook.make_item(item) + "\n"
            else:
                s += self.get_non_cookable_item(item) + "\n"
        return s
