import state
import state_a

class StateB(state.State):
    def handler(self, context):
        context.change_state(state_a.StateA())
        return 'State B'