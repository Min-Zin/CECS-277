import subject
import observer_a
def main():
    subj = subject.Subject()
    obsA = observer_a.ObserverA(subj)
    subj.state = "B" # ObsA->Subj State: B
    subj.detach(obsA)
    subj.state = "C" # ObsA->Subj State: C

main()