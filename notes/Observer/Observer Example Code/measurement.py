class Measurement:
    """
    Takes in a measurement in inches and broadcasts any updates to the
    number of inches to all conversion observers.
    """

    def __init__(self):
        self._inches = 0
        self._observers = []

    @property
    def inches(self):
        return self._inches

    @inches.setter
    def inches(self, new_inches):
        self._inches = new_inches
        self._notify_observer()

    def attach (self, observer):
        self._observers.append(observer)

    def detach (self, observer):
        self._observers.remove(observer)

    def _notify_observer(self):
        for obs in self._observers:
            obs.update()

    