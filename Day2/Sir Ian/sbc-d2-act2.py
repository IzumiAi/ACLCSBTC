import random

def get_choices():
    return random.randint(0, 1)

def determine_winner(choices):
    if len(set(choices)) == 1:
        return "None, continue the game!."
    else:
        winner = choices.index(min(set(choices), key = choices.count))
        if winner == 0:
            return "Player 1"
        elif winner == 1:
            return "Computer 2"
        else:
            return "Computer 3"

def play_game():
    player_choice = int(input())
    computer_choices = [get_choices() for _ in range(2)]
    choices = [player_choice] + computer_choices
    print("Player 1 choose: " + ("Fold" if player_choice == 0 else "Unfold"))
    print("Computer 2 choose: " + ("Fold" if computer_choices[0] == 0 else "Unfold"))         
    print("Computer 3 choose: " + ("Fold" if computer_choices[0] == 0 else "Unfold")) 
    winner = determine_winner(choices)
    if winner == "None":
        print(winner + " wins! balaa gud nimo")
    else:
        print(winner + " wins!")

if __name__ == "__main__":
    play_game()

