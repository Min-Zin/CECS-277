import componentA
import decoratorA

def main():
    obj = componentA.ComponentA()
    obj = decoratorA.DecorationA(obj)
    obj = decoratorA.DecorationA(obj)

    print(obj.operation()) # CompA DecA DecA

main()