import random

def game():
    player_choice = input("Enter Rock,Paper,or Scissor: ")
    possible_choices = ["Rock", "Paper", "Scissor"]
    computer_choice = random.choice(possible_choices)

    print("Your choice is : ",player_choice)
    print("Computer choice is : ",computer_choice)

    if player_choice == computer_choice:
        print("Both players selected ",player_choice,".It's a tie!")
    elif player_choice == "Rock":
        if computer_choice == "Scissor":
            print("Rock beats scissors! You won!")
        else:
            print("Paper beats rock! You lost.")
    elif player_choice == "Paper":
        if computer_choice == "Rock":
            print("Paper beats rock! You won!")
        else:
            print("Scissors beats paper! You lost.")
    elif player_choice == "Scissor":
        if computer_choice == "paper":
            print("Scissors beats paper! You won!")
        else:
            print("Rock beats scissors! You lost.")

    play_again = input("Play again? (yes/no): ")
    if play_again.lower() == "yes":
        game()
game()