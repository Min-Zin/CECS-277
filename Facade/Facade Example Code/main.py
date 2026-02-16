import restaurant_facade

def main():
    r = restaurant_facade.RestaurantFacade()
    choice = ""
    while choice != "Q":
        print(r.get_menu() + "Q. Complete Order" )
        choice = input("Enter Choice: ")
        print()
        if choice == "1":
            r.order_item("Hamburger")
        elif choice == "2":
            r.order_item("Fries")
        elif choice == "3":
            r.order_item("Drink")
        elif choice == "Q":
            tot = r.calc_total()
            print("Your total is: $" + str(tot))
    print("\nThank you!\nHere's your order: \n"+str(r.get_order()))

main()