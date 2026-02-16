Decorator Design Pattern:
    Decorator:
        - A structural design pattern used to dynamically add additional behaviors and responsibility to objects by chaining features together.
    
    Purpose:
        - Offers an alternative to subclassing, avoiding an overload of subclasses (e.g., combinations of pizza toppings). Ideal when modifications to the original class are not possible but additional behaviors are needed.
    
    Key Features:
        1. Encapsulation in Wrapper Interface:
            - Base object is warpped in an interface of the same type, which layers additional behaviours using a recursive-like method.
            - Once decorated, the object is no longer of the base type and cannot access methods exclusive to that class, but it can still use methods from the component type.
    
    Decorator Structure (UML Components):
        1. Component Interface:
            - Defines methods that all base objects and decorators need to implement.

        2. Concrete Component Classes:
            - Implement the Component Interface and override its methods.
            - Serve as teh base object which will be decorated.
        
        3. Abstract Decorator Class:
            - Implements the Component Interface.
            - Contains an instance of a component object, initialize through the constructor (init method)

        4. Concrete Decorator Classes:
            - Extend the Abstract Decorator.
            - Override methods of the Component Interface, calling the superclass's method and adding extra functionality for sepcific decorations.

    Benefits:
        1. Flexible Extension
            - Allows dynamic addition of responsibilities without altering the original class.

        2. Reduced Subclassing
            - Minimizes the need for numerous subclasses to cover combinations of behaviors or properties.

        3. Modular Decoration
            - Each decorator can add specific functionality, making the pattern useful for objects requiring multiple, indepent features.