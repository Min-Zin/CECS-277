import state_off
import state_pop
import radio_state

class StateOldies(radio_state.RadioState):
    def turn_on(self, radio):
        return "Radio is already on..."
    
    def trun_off(self, radio):
        return "Truning radio off..."
    
    def change_station(self, radio):
        radio.change_state(state_pop.StatePop())
        return "Station -> Pop"
    
    