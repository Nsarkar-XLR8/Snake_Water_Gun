import random

def get_user_choice():
    while True:
        user_choice = input("Enter Snake, Water, or Gun: ").lower()
        if user_choice in ['snake', 'water', 'gun']:
            return user_choice
        else:
            print("Invalid choice. Please enter Snake, Water, or Gun.")

def get_computer_choice():
    choices = ["snake", "water", "gun"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's A Tie!")
    elif (user_choice == "gun" and computer_choice == "snake") or \
            (user_choice == "snake" and computer_choice == "water") or \
            (user_choice == "water" and computer_choice == "gun"):
        return "You Win!"
    else:
        return "Computer Wins!"

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Your choice is {user_choice} and computer choice is {computer_choice}")
        winner = determine_winner(user_choice, computer_choice)
        print(winner)

        play_again = input("Do you want to play? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Start The Game
play_game()
