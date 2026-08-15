import random

emojis = {"r": "🪨", "p": "📄", "s": "✂️"}
choices = ("r", "p", "s")

def get_user_choice():
    while True:
        user_choice = input("Rock, Paper, or Scissors? (r/p/s)").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice!")

def display_choices(user_choice, pc_choice):
    print(f"You chose: {emojis[user_choice]}")
    print(f"PC chose: {emojis[pc_choice]}")


def determine_winner(user_choice, pc_choice):
    if user_choice == pc_choice:
        print('Tie!')
    elif ( 
        (user_choice == 'r' and pc_choice == 's') or
        (user_choice == 's' and pc_choice == 'p') or
        (user_choice == 'p' and pc_choice == 'r')):
        print("You win!")
    else:
        print("You lose!")

def play_game():
    while True:
        user_choice = get_user_choice() 
        pc_choice = random.choice(choices)
        display_choices(user_choice, pc_choice)
        determine_winner(user_choice, pc_choice)

        keep_going = input("Wanna keep going? (y/n)").lower()
        if keep_going == 'n':
            break

play_game()