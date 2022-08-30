from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def is_valid_choice(choice, menu):
    choices = menu.get_items().split('/')
    choices.append('off')
    choices.append('report')
    return choice in choices

def run():
    machine_on = True
    machine_menu = Menu()
    machine = CoffeeMaker()
    cashier = MoneyMachine()
    while(machine_on):
        choice = ask_user_for_input(machine_menu)
        if choice == "off":
            machine_on = False
        elif choice == "report":
            machine.report()
            cashier.report()
        else:
            choice = get_menu_item(machine_menu, choice)
            if machine.is_resource_sufficient(choice):
                if cashier.make_payment(choice.cost):
                    machine.make_coffee(choice)

def ask_user_for_input(machine_menu):
    choice = "lalalala"
    while(not is_valid_choice(choice, machine_menu)):
        choice = input(f"What would you like? {machine_menu.get_items()}? ").lower()
    return choice


def get_menu_item(machine_menu, choice):
    menu_item = ''
    for item in machine_menu.menu:
        if item.name == choice:
            menu_item = item

    return menu_item

run()
