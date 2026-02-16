import menu
import cashier
import cook

class RestaurantFacade:
    """Facade to simplify the restaurant interface.
    Attributes:
        menu (Menu) - restaurant menu
        cook (Cook) - restaurant cook
        cashier (Cashier) - restaurant cashier
    """
    def __init__(self):
        """Constructs the menu, cook, and cashier"""
        self._menu = menu.Menu()
        self._cook = cook.Cook()
        self._cashier = cashier.Cashier(self._cook)

    def get_menu(self):
        """Returns a string with each of the menu items."""
        s = ""
        for i in range(len(self._menu)):
            s += str(i + 1) + ". " + str(self._menu[i]) + '\n'
        return s

    def order_item(self, item_name):
        """Adds an item to the order."""
        item = self._menu.get_item_by_name(item_name)
        self._cashier.add_item(item)
        if item.is_cookable():
            self._cook.add_cookable_item(item)

    def calc_total(self):
        """Calculates the total cost of the order."""
        return self._cashier.calc_total()

    def get_order(self):
        """Returns the completed order."""
        return self._cashier.bag_order()