import num_list

def main():
    list = num_list.NumList()
    for n in list:
        for m in list:
            print(m, end = " ")     # 1 2 3 4 5
        print()
        
main()