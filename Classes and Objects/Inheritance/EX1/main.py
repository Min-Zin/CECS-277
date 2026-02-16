import person
import employee

def main():
    p1 = person.Person("John", "123 Fake St.", 1999)
    p2 = employee.Employee("George", "456 Main St.", 1995, "System Admin", 80000)

    print(p1)
    print(p2)

main()