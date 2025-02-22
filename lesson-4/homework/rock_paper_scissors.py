import random

def get_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

def play_game():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    print("Rock, Paper, Scissors - First to 5 wins!")

    while player_score < 5 and computer_score < 5:
        player_choice = input("\nEnter rock, paper, or scissors: ").strip().lower()

        if player_choice not in choices:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        winner = get_winner(player_choice, computer_choice)
        
        if winner == "player":
            player_score += 1
            print("You win this round!")
        elif winner == "computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a draw!")

        print(f"Score - You: {player_score}, Computer: {computer_score}")

    if player_score == 5:
        print("\nCongratulations! You won the match!")
    else:
        print("\nComputer wins the match. Better luck next time!")

if name == "main":
    play_game()