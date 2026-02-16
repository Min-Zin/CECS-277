import decorator
class Pepperoni(decorator.Decorator):
    def get_price(self):
        return super().get_price() + 1

    def get_description(self):
        return super().get_description(), "Pepperoni "