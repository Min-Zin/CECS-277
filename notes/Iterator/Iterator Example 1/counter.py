class Counter:
    def __init__(self, max):
        self._max = max

    def __iter__(self):
        self._n = 0
        return self

    def __next__(self):
        self._n += 1
        if self._n > self._max:
            raise StopIteration
        else:
            return self._n