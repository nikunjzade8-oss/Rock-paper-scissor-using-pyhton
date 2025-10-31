import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win! 🎉"
    else:
        return "Computer wins! 💻"

def main():
    print("=== Rock Paper Scissors Game ===")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    
    user_choice = input("Your choice: ").lower()
    
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return
    
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    result = get_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
