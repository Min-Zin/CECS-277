import meters_observer
import feet_observer
import smoots_observer
import measurement

def main():
    meas = measurement.Measurement()
    feet = feet_observer.FeetObserver(meas)
    met = meters_observer.MetersObserver(meas)
    smoot = smoots_observer.SmootsObserver(meas)

    done = False
    while (not done):
        val = input("Enter measurement in inches (or Q to quit): ")

        if val == "Q" or val == "q":
            print("Quitting now")
            done = True
        else:
            meas.inches = float(val)
        print()

main()