import random

def play_game():
    options = ["rock", "paper", "scissors"]
    user_wins = 0
    computer_wins = 0

    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = input(
            "\nEnter rock, paper, or scissors (or 'quit' to stop): "
        ).lower()

        if user_choice == "quit":
            break

        if user_choice not in options:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win!")
            user_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1

        print(f"Score → You: {user_wins}, Computer: {computer_wins}")

    print("\nFinal Score:")
    print(f"You: {user_wins} | Computer: {computer_wins}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()