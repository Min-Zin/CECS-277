import abc
class Pizza(abc.ABC):
    @abc.abstractmethod
    def get_price(self):
        pass

    @abc.abstractmethod
    def get_description(self):
        pass