import random

def get_choices():
    return random.randint("hayang", "kulob")

def determine_winner(choices):
    if len(set(choices)) == 1:
        return "None, continue the game!."
    else:
        winner = choices.index(min(set(choices), key = choices.count))
        if winner == ("hayang"):
            return "Player 1"
        elif winner == ("kulob"):
            return "Computer 2"
        else:
            return "Computer 3"

def play_game():
    player_choice = int("hayang or kulob?: ")
    computer_choices = [get_choices() for _ in range(2)]
    choices = [player_choice] + computer_choices
    print("Player 1 choose: " + ("Fold" if player_choice == "hayang" else "Unfold"))
    print("Computer 2 choose: " + ("Fold" if computer_choices["hayang"] == "hayang" else "Unfold"))         
    print("Computer 3 choose: " + ("Fold" if computer_choices["hayang"] == "hayang" else "Unfold")) 
    winner = determine_winner(choices)
    if winner == "None":
        print(winner + " wins! balaa gud nimo")
    else:
        print(winner + " wins!")

if __name__ == "__main__":
    play_game()

