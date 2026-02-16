from puppy_state import PuppyState
import state_asleep

class StatePlay(PuppyState):
    def feed(self, puppy):
        return "The puppy is too busy playing with the ball to eat right now."

    def play(self, puppy):
        puppy.inc_plays()
        if puppy._plays > 2:
            puppy.reset()
            puppy.change_state(state_asleep.StateAsleep())
            return "The puppy played so much it fell asleep!"
        else:
            return "You throw the ball again and the puppy exictedly chases it."