import observer
class ObserverA(observer.Observer):
    def __init__(self, subject):
        self._subject = subject
        self._subject.attach(self)

    def update(self):
        print("ObsA -> Subj State: " + self._subject.state)