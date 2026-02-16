import check_input
from player import Player

def take_turn(player):
    """"
    - Roll the player's dice
    - Display the dice
    - Check for and display any win types (pairs, series, three of a kind)
    - Display updated score
    """
    player.roll_dice()

    print(f'You rolled: {player}')
    
    if player.has_three_of_a_kind():
        print("Three of a kind! +3 points")
    elif player.has_pair():
        print("You got a pair! +3 points")
    elif player.has_series():
        print("You got a series! + 2 points")

    print (f'Your current score is: {player.get_points()} points\n')

def main():
    """
    - Construct a Player object
    Repeatedly call take_turn
    """
    player = Player()
    while True:
        take_turn(player)

        continue_game = check_input.get_yes_no("Do you want to roll again> (Y/N): ")

        if not continue_game:
            break

    print(f'Game over! Your final socre is {player.get_points()} points.')

if __name__ == "__main__":
    main()