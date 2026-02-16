class NumList:
    def __init__(self):
        self._nums = [1,2,3,4,5]

    def __iter__(self):
        return ListIterator(self)

class ListIterator:
    def __init__(self, num_list_obj):
        self._num_list = num_list_obj
        self._i = -1

    def __next__(self):
        self._i += 1
        if self._i >= len(self._num_list._nums):
            raise StopIteration
        else:
            return self._num_list._nums[self._i]
        