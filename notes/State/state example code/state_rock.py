import state_off
import state_oldies
import radio_state

class StateRock(radio_state.RadioState):
    def turn_on(self, radio):
        return "Radio is already on..."
    
    def turn_off(self, radio):
        radio.change_state(state_off.StateOff())
        return "Turning radio off..."
    
    def change_station(self, radio):
        radio.change_state(state_oldies.StateOldies())
        return "Station -> Oldies"
    