import conversion_observer

class MetersObserver(conversion_observer.ConversionObserver):
    def __init__(self, subject):
        self._subject = subject
        self._subject.attach(self)

    def update(self):
        meters = self._subject.inches / 39.37
        print("Meters = " + str(meters))

    