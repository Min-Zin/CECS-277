import abc

class Component(abc.ABC):
    @abc.abstractclassmethod
    def operation(self):
        pass
