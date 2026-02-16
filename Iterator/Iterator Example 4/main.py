import num_list

def main():
    list = num_list.NumList()
    for n in list:
        for m in list:
            print(m, end=" ")   # 1 2 3 4 5 
        print()                 # 1 2 3 4 5
                                # 1 2 3 4 5 
main()                          # 1 2 3 4 5
                                # 1 2 3 4 5