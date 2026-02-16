import num_list

def main():
    list = num_list.NumList()
    for a in list.get_backwards_iterator():
        print(a, end=" ") # 5 4 3 2 1

main()