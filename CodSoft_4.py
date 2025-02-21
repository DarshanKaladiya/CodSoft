import random

class Rockpaperscissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.user_score = 0
        self.computer_score = 0
        self.rounds = 0

    def play(self):
        print("Welcome to Rock Paper Scissors Game")
        print("Enter 'rock', 'paper', 'scissors' to play")
        while True:
            user_choice = input("\nEnter your choice: ").lower()
            if user_choice not in self.choices:
                print("\nInvalid choice. Please enter 'rock', 'paper', 'scissors'")
                continue
            computer_choice = random.choice(self.choices)
            print(f"Computer choice: {computer_choice}")
            if user_choice == computer_choice:
                print("It's a tie")
            elif user_choice == "rock" and computer_choice == "scissors":
                print("You win")
                self.user_score += 1
            elif user_choice == "scissors" and computer_choice == "paper":
                print("You win")
                self.user_score += 1
            elif user_choice == "paper" and computer_choice == "rock":
                print("You win")
                self.user_score += 1
            else:
                print("Computer wins")
                self.computer_score += 1
            self.rounds += 1
            print(f"\nScore: User {self.user_score} - {self.computer_score} Computer")
            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                print(f"\nGame Over. You played {self.rounds} rounds")
                break

if __name__ == "__main__":
    game = Rockpaperscissors()
    game.play()