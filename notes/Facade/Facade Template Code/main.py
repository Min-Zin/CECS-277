"""
The facade constructs the objects necessary to perform the tasks 
needed by the client and then uses  the objects to accomplish the task.
The facade helps to minimize the dependencies in the client.
"""

import facade

def main():
    f = facade.Facade()
    print(f.operation())

main()