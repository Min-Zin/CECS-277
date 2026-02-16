Inheritance [EX1]:
    When you create a new class that is derived from an existing class.
    Anything that has an "is a" relationship is usually inheritance.
    Example:
        A dog "is an" Animal
    
    Inheritance allows variables and methods from existing class to become a part of the new extended class, this helps cut donw on a lot of duplicated code.

    The derived class (subclass) identifies which class it is inheriting from by placing the name of the existing class (the superclass) in a set of parentheses.
        Example:
            class Employee(Person)
    
    This is one directional, meaning that an Employee "is an" Person, but not all Person objects are Employees.

    Similarly, the Empoyee class can be extended into different types of employees.
        Example:
            class Engineers(Employee)
            class Secretaries(Employees)
            class Accountant(Employees)
    
    This frees the programmer from having to write and test similar functions for each of the different types of classes. Additionally, if any modifications need to be made, it can be done to the superclass, rather than trying to figure out everywhere you might have made a similar method.