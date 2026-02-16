import state_rock
import radio_state

class StateOff(radio_state.RadioState):
    def turn_on(self, radio):
        radio.change_state(state_rock.StateRock())
        return "Turning radio on...\nStation -> Rock"
    
    def turn_off(self, radio):
        return "Radio is already off..."
    
    def change_station(self, radio):
        return "Radio must be on to change station."
    
    