MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def is_valid_choice(choice):
    choices = list(MENU.keys())
    choices.append('off')
    choices.append('report')
    return choice in choices

def run():
    machine_on = True
    current_resources = resources
    while(machine_on):
        choice = ask_user_for_input()
        if choice == "off":
            machine_on = False
        elif choice == "report":
            print_resources(current_resources)
        else:
            current_resources = serve_coffee(choice, current_resources)

def ask_user_for_input():
    choice = "lalalala"
    while(not is_valid_choice(choice)):
        choice = input("What would you like? (espresso/latte/cappuccino)").lower()
    return choice

def print_resources(current_resources):
    print(f"Water: {resources['water']} mL")
    print(f"Milk: {resources['milk']} mL")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: {resources['money']}$")

def serve_coffee(choice, current_resources):
    if check_resources(choice, current_resources):
        provided_money = ask_for_money(choice)
        price = MENU[choice]["cost"]
        if price > provided_money:
            print("Not enough money, refunding.")
        else:
            change = round(provided_money - price, 2)
            print(f"Here's your {choice} and some change: {change}$")
            current_resources = adjust_resources(current_resources, choice)
    else:
        print("Not enough resources!")
    return current_resources

def check_resources(choice, current_resources):
    valid = True
    for resource in MENU[choice]["ingredients"]:
        needed = MENU[choice]["ingredients"][resource]
        current = current_resources[resource]
        valid = valid and current >= needed
    return valid

def ask_for_money(choice):
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    paying = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return paying

def adjust_resources(current_resources, choice):
    for resource in MENU[choice]["ingredients"]:
        current_resources[resource] -= MENU[choice]["ingredients"][resource]
    current_resources["money"] += MENU[choice]["cost"]
    return current_resources

run()
