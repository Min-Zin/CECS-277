import state_a
class Context:
    def __init__(self):
        self._state = state_a.StateA()

    def change_state(self, state):
        self._state = state

    def request(self):
        return self._state.handler(self)