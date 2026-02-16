import radio

def main():
    r = radio.Radio()
    opt = 0
    
    while opt != 4:
        opt = input("1. Off\n2. On\n3. Channel\n4. Quit\n")

        if opt == 1:
            print(r.off_switch())
        
        elif opt == 2:
            print(r.on_switch())
        
        elif opt == 3:
            print(r.channel_switch())

main()