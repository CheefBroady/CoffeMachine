import os
# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
is_on = True

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

coinvalue = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "pennie": 0.01
}

# Functions
def clear_screen():
    """clear screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def check_resources(product):
    """Check resources sufficient? a. When the user chooses a drink, the program should check
     if there are enough resources to make that drink.
     when the process has been accomplished
     add price and subtract ingredients, depenedet of the selected product"""
    for item in MENU[product]['ingredients']:
        if resources[item] < MENU[product]['ingredients'][item]:
            print(f"Sorry there is not enough {item}.")
            return
    insert_coins = calc_coins(product)
    if insert_coins > 0:
        resources['money'] += insert_coins # MENU[product]['cost']
        for item in MENU[product]['ingredients']:
            resources[item] -= MENU[product]['ingredients'][item]
        # calculate the coins needed


def get_price(product):
    """Returns the price of the selected product"""
    return MENU[product]['cost']


def calc_coins(product):
    """Returns the value of entered coins when it has accomplished the ordering process or 0 when its wrong.
    The program prompt the user to insert coins and calculates the monetary value of the coins insert
    and check that the user has inserted enough money to purchase the drink they selected - Possible values to insert:
    quarter = $0.25, dime = $0.10, nickel = $0.05, pennie = $0.01"""
    insert_value = 0
    price = get_price(product)
    print("Possible coins to insert: quarter = $0.25, dime = $0.10, nickel = $0.05, pennie = $0.01!")
    while insert_value < price:
        # coin_type = False
        insert_value = int(input("Number of quarter insert: ")) * 0.25
        insert_value += int(input("Number of quarter insert: ")) * 0.10
        insert_value += int(input("Number of quarter insert: ")) * 0.05
        insert_value += int(input("Number of quarter insert: ")) * 0.01
        # insert = input("Type in a coin: ")
        # for coin in coinvalue:
        #    if insert == coin:
        #        coin_type = True
        #        insert_value += coinvalue[insert]
        #        print(f"Insert value: $ {insert_value}")
        #        break
        # if coin_type is False and insert_value < price:
        if insert_value < price:
            print(f"Sorry that's not enough money. Money refunded.")
            return 0
        elif insert_value > price:
            print(f"Here is $ {round(insert_value - price, 2)} dollars in change.")
            print(f"Here is your {product}. Enjoy!")
            return price
        elif insert_value == price:
            print(f"Here is your {product}. Enjoy!")
            return price


def return_report():
    """Returns a report of the current resources as an inventory status"""
    unit = "ml"
    for item in resources:
        if item == "coffee":
            unit = "g"
            print(f"{item}: {resources[item]} {unit}")
        elif item == "money":
            print(f"{item.capitalize()}: $ {resources[item]}")
        else:
            print(f"{item}: {resources[item]} {unit}")


# Program
while is_on:
    """Check the user’s input to decide what to do next."""
    clear_screen()
    print(f"\nMenu:")
    for value in MENU:
        print(f"{value.capitalize()} = $ {MENU[value]['cost']}")
    selected_item = input(f"\nWhat would you like?\n").lower()
    if selected_item == "off":
        is_on = False
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
    clear_screen()
