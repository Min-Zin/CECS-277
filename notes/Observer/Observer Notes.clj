Observer:
    - A behavioral design pattern that allows an object to notify other
    objects whenever its's state has changed, or an event has occured.
    - This type of interaction is also known as publish-subscribe, where
    a subject publishes notifications about its state change and automatically
    sends them out to each subscribing object.

    Contains 3 main classes:
        1. Subject class:
            - Class that has a state and maintains a list of observers
            that will be notified whenever its state changes.

        2. Observer Interface:
            - has an update method taht is overridden by the impementing
            Observer classes and is called by the Subject when its state
            changes.

        3. Concrete Observer class:
            - Contains an instance of the Subject that they are observing
            so that when the notification comes in that the state has change,
            they may call the Subject's methods to find out more about the
            Subject's updated state.

            