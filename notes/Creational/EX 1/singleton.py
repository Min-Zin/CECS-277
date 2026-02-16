"""
A single ton consist of variable that holds the instance once its created
and an overridden __new__ method.
"""

class  Singleton:
    _instance = None
    _initialized = False

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, x):
        if not Singleton._initialized:
            self._x = x
            Singleton._initialized = True
    
    def inc_x(self):
        self._x += 1

    def __str__(self):
        return super().__str__() + "x = " + str(self._x)
    
