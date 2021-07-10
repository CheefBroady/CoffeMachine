import os
# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
no_maintenance = True

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

# Functions
def clear_screen():
    """clear screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def check_resources(product):
    """Check resources sufficient? a. When the user chooses a drink, the program should check
     if there are enough resources to make that drink."""
    for item in MENU[product]['ingredients']:
        if resources[item] < MENU[product]['ingredients'][item]:
            print(f"Sorry there is not enough {item}.")
            return
    resources['money'] += MENU[product]['cost']
    for item in MENU[product]['ingredients']:
        resources[item] -= MENU[product]['ingredients'][item]
    # for item in resources:
    #    print(f"neuer Wert für {item} = {resources[item]}")


def get_price(product):
    """get the price of the selected coffee"""
    return MENU[product]['cost']


def return_report():
    """return a report of the current resources as an inventory status"""
    unit = "ml"
    for item in resources:
        if item == "coffee":
            print(f"{item}: {resources[item]} g")
        elif item == "money":
            print(f"{item.capitalize()}: $ {resources[item]}")
        else:
            print(f"{item}: {resources[item]} {unit}")


while no_maintenance:
    """Check the user’s input to decide what to do next."""
    clear_screen()
    print(f"\nMenu:")
    for value in MENU:
        print(f"{value.capitalize()} = $ {MENU[value]['cost']}")
    selected_item = input(f"\nWhat would you like?\n").lower()
    if selected_item == "off":
        no_maintenance = False
        print("Bye bye")
    elif selected_item == "report":
        return_report()
    elif selected_item == "latte":
        print(f"You selected {selected_item.capitalize()} for $ {get_price(selected_item)}")
        check_resources(selected_item)
    elif selected_item == "espresso":
        print(f"You selected {selected_item.capitalize()} for $ {get_price(selected_item)}")
        check_resources(selected_item)
    elif selected_item == "cappuccino":
        print(f"You selected {selected_item.capitalize()} for $ {get_price(selected_item)}")
        check_resources(selected_item)
    else:
        print("Wrong entry, please try it again!")


# TODO: 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52


# TODO: 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that# s not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.


# TODO: 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink