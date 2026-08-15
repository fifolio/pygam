import random

number_to_guess = random.randint(1, 100)

while True:

    try:
        guess = int(input('Guess the number between 1 and 100: '))

        if guess < number_to_guess:
            print("Too Low")
        elif guess > number_to_guess:
            print("Too Hight")
        else: 
            print("Congratulations! you guessed the number")
            break
    except ValueError:
        print("Only a valid number")

    print(guess)