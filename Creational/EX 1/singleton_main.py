import singleton

def main():
    s1 = singleton.Singleton(1)
    s2 = singleton.Singleton(5)

    print(s1)      #0x0f70 x = 1
    print(s2)       #0x0f70 x = 1

    s1.inc_x()
    print(s1)     #0x0f70 x = 2
    print(s2)     #0x0f70 x = 2
    
    s2.inc_x()
    print(s1)     #0x0f70 x = 3
    print(s2)     #0x0f70 x = 3

main()