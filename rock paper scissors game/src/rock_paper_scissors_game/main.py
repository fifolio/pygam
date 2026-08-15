import random

emojis = {"r": "🪨", "p": "📄", "s": "✂️"}
choices = ("r", "p", "s")

while True:
    user_choice = input("Rock, Paper, or Scissors? (r/p/s)").lower()
    if user_choice not in choices:
        print("Invalid choice!")
        continue

    pc_choice = random.choice(choices)

    print(f"You chose: {emojis[user_choice]}")
    print(f"PC chose: {emojis[pc_choice]}")

    if user_choice == pc_choice:
        print('Tie!')
    elif ( 
        (user_choice == 'r' and pc_choice == 's') or
        (user_choice == 's' and pc_choice == 'p') or
        (user_choice == 'p' and pc_choice == 'r')):
        print("You win!")
    else:
        print("You lose!")

    keep_going = input("Wanna keep going? (y/n)").lower()
    if keep_going == 'n':
        break