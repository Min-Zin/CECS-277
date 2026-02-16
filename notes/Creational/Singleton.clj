Singleton
    Design Patterns:
        are general solutions to common problems that come up when designing software.
        They are also commonly used as a means of communication (like idioms) between programmers about the design.
        Being familiar with them can help you efficiently build applications that are easier to maintain by using clearly 
        defined approaches rather than reinventing a solution from scratch.

    In 1994, four authors, Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides (more commonly known as the Gang of 
    Four (GoF)), published a book describing 23 different design patters with descriptions, examples, template code, and UML 
    diagrams.  They were interested in reusable object:oriented design and noticed that programmers often came up with similar
    solutions to commonly recurring problems and thought it would useful if programmers everywhere knew about these patterns.

    These patterns are general solutions to common problems, they do not consist of code that you can copy and paste into your 
    program and have them work. The patterns must be adapted to fit your problem. Do not try to adapt your problem to fit a pattern.

    Types of Design Patterns:

        1. Creational:
            these patterns provide a systematic way of creating objects. They use interfaces and polymorphism to allow the construction 
            process to be more dynamic and flexible of which, when, and how objects are initialized.

        2. Structural:
            these patterns are used to define and build relationships between classes to form them into a larger structure that is 
            flexible and extensible.  They use inheritance and interfaces to get classes to work together to form a single working item.
            They help make sure that if one part changes, the rest of the structure doesn't need to be changed as well.

        3. Behavioral:
            these patterns make for better interactions and communications between objects by assigning responsibilities to a class.

    Singleton [EX 1, EX 2]:
        a creational design pattern.

        Singleton is the smallest, simplest, and one of the more commonly used design patterns. It is used to make sure that there is, 
        at most, only ever a single instance of the class that is used throughout the entire program and provides a global access point to it.
        It's primarily used when you need global access to a single shared resource, such as a file or a database (especially if it is resource 
        intensive to open).

        To ensure that only one object is ever created, access to the constructor is usually limited by making it private, however, in Python, 
        there is no way to make something completely private. Instead, we can override the __new__ method, which is the method that is called 
        before the __init__ method is called when constructing new objects. There, we can check to see if an instance has been created, if it has,
        then return that one, if not, allow it to construct one. One problem with this is that the init method will always be called whether a new 
        object was constructed or not, so another class variable is used to check to see if the object was already initialized.

    