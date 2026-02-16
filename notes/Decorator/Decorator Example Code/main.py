import small_pizza
import large_pizza
import pepperoni
import mushroom

def main():
    p = small_pizza.PizzaSmall()
    p = mushroom.Mushrooms(p)
    p = pepperoni.Pepperoni(p)

    print(p.get_description())
    print(p.get_price())

main()