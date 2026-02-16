import state
import state_b

class StateA(state.State):
    def handler(self, context):
        context.change_state(state_b.StateB())
        return 'State A'