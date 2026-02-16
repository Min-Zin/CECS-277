import decorator

class Mushroom(decorator.Decorator):
    def get_description(self):
        return super().get_description(), "Mushrooms"
    
    def get_price(self):
        return super().get_price() + .5