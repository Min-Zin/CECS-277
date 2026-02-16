class NumList:
    def __init__(self):
        self._nums = [1, 2, 3, 4, 5]
    
    def __iter__(self):
        self._i = 0
        return self
    
    def __next__(self):
        if self._i < len(self._nums):
            val = self._nums[self._i]
            self._i += 1
            return val
        else:
            raise StopIteration
    