import conversion_observer

class FeetObserver(conversion_observer.ConversionObserver):
    def __init__(self, subject):
        self._subject = subject
        self._subject.attach(self)

    def update(self):
        feets = self._subject.inches / 12
        print("Feets = " + str(feets))

    