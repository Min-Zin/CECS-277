import abc
import pizza

class Decorator(pizza.Pizza, abc.ABC):
    def __init__(self, p):
        self._pizza = p
    
    def get_price(self):
        return self._pizza.get_price()
    
    def get_description(self):
        return self._pizza.get_description()
    
    