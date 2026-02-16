Memento:
    - Behavioral design pattern
    - Allows object to revert to previous state.
    - Commonly used to implement an 'undo' feature in a program

    - Consist of 3 parts:
        1. Originator:
            - is an object that has a state that needs to be saved
            and eventually reverted back to.
        
        2. Memento:
            - stores the values that present the previous state of
            the Originator.
        
        3. Caretaker:
            - which controls the originator's state and stores the 
            Memento
    
        [Originator] is in charge of creating its own [Mementos], but
        the [Caretaker] specifies when those [Mementos] should be saved 
        and when the [Originator] should use them to revert a previous
        state.

    