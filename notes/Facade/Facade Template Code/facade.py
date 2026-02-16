import subA
import subB
import subC

class Facade:
    def operation(self):
        sa = subA.SubA()
        sb = subB.SubB()
        sc = subC.SubC()
        return sa.operationA() + " " + sb.operationB() + " " + sc.operationC()