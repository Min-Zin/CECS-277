import random

def display_list(list):
    """Displays the list."""
    for i in range(len(list)-1):
        print(list[i], end=" ") # breakpoint
    print()
            
def main():
    list = [1,2,3,4,5]
    display_list(list)

main()