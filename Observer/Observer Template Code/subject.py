class Subject:
    def __init__(self):
        self._state = "A"
        self._observers = []

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        self._state = new_state
        self._notify_observers()

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def _notify_observers(self):
        for obs in self._observers:
            obs.update()
