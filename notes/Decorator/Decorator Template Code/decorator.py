import abc
import component

class Decorator(component.Component, abc.ABC):
    def __init__(self, comp):
        self._component = comp
    
    def operation(self):
        return self._component.operation()
    