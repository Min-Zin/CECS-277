import memento
class Originator:
    def __init__(self):
        self._state = 0

    @property
    def state(self):
        return self._state

    def change_state(self):
        self._state += 1

    def save(self):
        return memento.Memento(self._state)

    def restore(self, mem):
        self._state = mem.get_state()