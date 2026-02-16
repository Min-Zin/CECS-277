Iterator [EX 1, 2]:
    A behavioral design pattern that enables traversal of elements in a collection
    (e.g., lists, trees, dictionaries) without exposing the collection's internal 
    structure. It defines a standard way to sequentially access elements, making 
    it possible to use different traversal algorithms (e.g., depth-first or 
    breadth-first for trees).

Python Iterators: 
    In Python, iterators are built into the language.
    
To make an object iterable:

    1. Implement the [__iter__] method: This initializes variables needed for iteration 
    and returns the iterator object (often self).

    2. Implement the [__next__] method: This returns the next item in the sequence and 
    raises a StopIteration exception when the sequence ends.

Once these methods are defined, the collection can be iterated using a for loop.

---
Nested loops [EX 3]:
    one problem with EX 2, is that the iterator cannot be used simultaneously with another
    instance of the same iterator (ie. cannot be used in a nested loop). Instead, the [__next__]
    of the second instance (inner for loop) will iterate over the contents of the container
    and then there won't be any contents left for the first instance (outer for loop)

[EX 4]:
When you need to iterate through your collection using a nested loop, then you'll need to
create your iterator as a seperate class so that it can create multiple seperate instances.

---
Alternate Traversals:
    a benefit of creating your iterators in a separate class is that you can then create 
    multiple types of traversals and then be able to choose how you'd like to traverse 
    your collection. 