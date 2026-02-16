--Categories of Design Patterns--
    1. Creational:
        Focuses on the creation of objects.

    2. Structural: 
        Deals with the composition of classes or objects.

    3. Behavioral: 
        Concerned with the interaction and responsibility of objects.

--Creational Patterns--

    *Singleton
        - Purpose: 
            . Ensures a class has only one instance and provides a global 
            point of access to it.
        
        - Key Concepts:
            . Override the `new` method to restrict instance creation.
            . Maintain a class-level `_instance` variable to hold the
            single instance.

    *Factory Method
        - Purpose: 
            . Encapsulates the process of constructing objects to make the
            code more flexible.
        
        - Key Concepts:
            . Subclasses determine the specific class of the object that
            will be created.

            . Promotes loose coupling by delegating instantiation to 
            subclasses.

    *Abstract Factory
        - Purpose: 
            . Provides an interface for creating families of related or 
            dependent objects without specifying their concrete classes.
        
        - Key Concepts:
            . Often implemented as a set of factory methods grouped 
            into a single class.

            . Supports consistent creation of related products 
            (e.g., GUI components).


--Structural Patterns--

    *Decorator
        - Purpose: 
            . Dynamically attach additional behaviors or responsibilities
            to objects without modifying their code.
        
        - Key Concepts:
            . Uses composition to "wrap" an object.
            . Commonly used for adding features to GUI components.

    Adapter
        - Purpose: 
            . Allows incompatible interfaces to work together.
    
        - Key Concepts:
            . Acts as a bridge between two incompatible interfaces.

            . Converts the interface of a class into another interface
            expected by clients.

    Facade
    - Purpose:
        . Simplifies the interface of a complex subsystem.

    - Key Concepts:
        . Provides a unified interface to a set of interfaces in a subsystem.
        . Makes the subsystem easier to use by hiding its complexity.

--Behavioral Patterns--

    *Iterator
        - Purpose: Provides a way to access the elements of a collection sequentially
        without exposing its underlying representation.

        - Key Concepts:
            . Separates the traversal logic from the collection itself.
            . Supports different traversal methods (e.g., forward, backward).

    *State
        - Purpose: Encapsulates the state of an object, allowing it to alter its
        behavior when its state changes.

        - Key Concepts:
            . Uses state-specific classes to represent different states.
            . Context delegates state-dependent behavior to the current state object.

    Memento
        - Purpose: Captures and externalizes an object's state so that it can be 
        restored later without violating encapsulation.

        - Key Concepts:
            . Involves three main roles: Originator (creates the memento),
            Memento (stores the state), and Caretaker (manages the memento).

            . Useful for undo mechanisms.

    Observer
        - Purpose: Establishes a one-to-many dependency so that when one object's 
        state changes, all its dependents are notified.

        - Key Concepts:
            . The subject maintains a list of observers and notifies them of state changes.
            . Promotes loose coupling between the subject and its observers.

--Summary--
    . Understanding design patterns helps create robust, scalable, and maintainable software.
    This guide highlights the purpose, concepts, and applications of each pattern, categorized
    into Creational, Structural, and Behavioral groups. Focus on how each pattern solves 
    specific design problems and promotes software flexibility and reusability.

