import originator
def main():
    history = []
    o = originator.Originator() # 0

    print("Current State = " + str(o.state))

    o.change_state() # 1
    o.change_state() # 2
    print("Current State = " + str(o.state)) # 2
    

    history.append(o.save()) # saves state 2
    o.change_state() # 3
    o.change_state() # 4
    print("Current State = " + str(o.state)) # 4
    

    history.append(o.save()) # saves state 4
    o.change_state() # 5
    print("Current State = " + str(o.state)) # 5
    

    o.restore(history.pop(len(history) - 1)) # restores to state 4
    print("Current State = " + str(o.state)) # 4
    

    o.restore(history.pop(len(history) - 1)) # restores to state 2
    print("Current State = " + str(o.state)) # 2
    

main()