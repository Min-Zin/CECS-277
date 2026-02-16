import conversion_observer

class SmootsObserver(conversion_observer.ConversionObserver):
    def __init__(self, subject):
        self._subject = subject
        self._subject.attach(self)

    def update(self):
        smoots = self._subject.inches / 67
        print("Smoots = " + str(smoots))

    