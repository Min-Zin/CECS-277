class Memento:
    def __init__(self, s):
        self._state = s
    def get_state(self):
        return self._state