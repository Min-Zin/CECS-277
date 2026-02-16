import state_off
import state_rock
import radio_state

class StatePop(radio_state.RadioState):
    def turn_on(self, radio):
        return "Radio is already on..."
    
    def trun_off(self, radio):
        return "Truning radio off..."
    
    def change_station(self, radio):
        radio.change_state(state_rock.StateRock())
        return "Station -> Rock"
    
    