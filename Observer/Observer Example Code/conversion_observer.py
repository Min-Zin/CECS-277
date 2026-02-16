import abc

class ConversionObserver(abc.ABC):
    @abc.abstractmethod
    def update(self):
        pass

