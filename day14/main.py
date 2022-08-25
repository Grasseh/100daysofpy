import art
import game_data
import random
import os

def game_loop():
    score = -1
    previous_comparison = random.choice(game_data.data)
    loss = False

    while(not loss):
        score += 1
        previous_comparison, loss = new_round(previous_comparison, score)
        if loss:
            print(f"You are wrong! Final score: {score}")

def pull_data(previous):
    comparison = previous
    while(previous["name"] == comparison["name"]):
        comparison = random.choice(game_data.data)
    return comparison

def new_round(previous, score):
    os.system('clear')
    current = pull_data(previous)

    print(art.logo)
    if score > 0:
        print("You are correct!")
    print(f"Your current score is {score}.")
    print("")
    formatted_print('A', previous)
    print(art.vs)
    formatted_print('B', current)
    choice = get_user_choice()
    winner = 'a'
    if previous["follower_count"] < current["follower_count"]:
        winner = 'b'
    return [current, choice != winner]

def formatted_print(letter, choice):
    name = choice["name"]
    description = choice["description"]
    country = choice["country"]
    print(f"Compare {letter}: {name}, a {description} from {country}")

def get_user_choice():
    choice = "c"
    while(choice != "a" and choice != "b"):
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    return choice

game_loop()
