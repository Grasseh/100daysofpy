#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


def run():
    play()

def play():
    random_number = random.randint(1, 101)
    amount_guesses = 10
    if input("Press 'h' to play on hard mode. ").lower() == 'h':
        amount_guesses = 5
    win = False
    while(amount_guesses > 0 and not win):
        print(f"You have {amount_guesses} guesses remaining")
        guess = int(input("Take a guess! From 1 to 100! "))
        if guess > random_number:
            print("Too High!")
        elif guess < random_number:
            print("Too Low!")
        else:
            win = True
        amount_guesses -= 1
    if win:
        print("You win!")
    else:
        print("You lose!")
    print(f"The correct answer was {random_number}")

import art
import random
print(art.logo)
run()
