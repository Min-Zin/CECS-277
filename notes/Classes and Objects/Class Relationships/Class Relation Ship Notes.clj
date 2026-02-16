Class Relationships:
    When creating programs that hae several different classes, some of those classes will have connections and realtionships include:
        
        Dependency [EX 1]:
            . the case where class A "uses" an instance of class B.
            . An object of type B might be passed into one of class A's methods in order to use one of B's methods. 
            . It is often beneficial to minimize dependencies (or coupling) in your code.
            . Because, whenever B is modified, then A will usually need to be changed too.

            . UML:
                A "---->" B (DOTTED LINE)

        Aggregation [EX 2]:
            . the case where class A "has" one or more references to class B. 
            . An instance of class B is created elsewhere and then passed in and the reference is set.
            . Then, if class A is ever destroyed, any objects of type B that class A referenced will continue to exist wherever they were created.

            . UML:
                B "<>____" A(diamond followed by a solid line)
        
        Composition [EX 3, EX 5]:
            . is a stronger type of aggregation, where class A "owns" an instance of class B.
            . Class A constructs one or more instances of class B, so if A is ever destroyed, so are any instances of B that class A owned.

            .UML:
               B "<.>_____" A (filled diamond followed by a solid line)

        Inheritance [EX 4]:
            .  is he case where class B "is a" instance of class A. 
            . Class B is derived from class A, class B gains class A's attributes and methods, and then class B has its own specialized code.

            . UML:
                B "<|____" A (hollow arrow followed by a solid line)

        Interface:
            . UML:
                A "----|>" B