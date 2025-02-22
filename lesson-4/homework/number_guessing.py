import random

def play_game():
    while True:
        number = random.randint(1, 100)
        attempts = 10

        print("Guess a number between 1 and 100. You have 10 attempts.")

        for attempt in range(1, attempts + 1):
            try:
                guess = int(input(f"Attempt {attempt}: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print("You guessed it right!")
                return

        print("You lost. Want to play again? (Y/N)")
        retry = input().strip().lower()
        if retry not in ('y', 'yes', 'ok'):
            break

if name == "main":
    play_game()