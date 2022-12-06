import sys

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


def check_resources(selected_beverage):
    """return True if enough resources, False if not """
    for ingredient in MENU[selected_beverage]["ingredients"]:
        if resources[ingredient] < MENU[selected_beverage]["ingredients"][ingredient]:
            print(f"insufficient {ingredient}")
            return False
        return True


def payment():
    print("Please insert coins. ")
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input("How many nickles? "))
    pennies = float(input("How many pennies? "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def process_order(selected_beverage, money_paid):
    # deduct ingredients
    for ingredient in MENU[selected_beverage]["ingredients"]:
        resources[ingredient] -= MENU[selected_beverage]["ingredients"][ingredient]

    # give change
    change = money_paid - MENU[selected_beverage]["cost"]
    print(f"Here's {change} in change.")

    # give drink
    print(f"Here's your {selected_beverage} ☕ Enjoy!")


machine_on = True

while machine_on:
    beverage = input("What would you like? (espresso/latte/cappuccino): ")

    if beverage == "report":
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${resources["money"]}')
    elif beverage == "off":
        sys.exit("powering down...")
    else:
        # check resource
        if check_resources(beverage):
            # if there's enough resources, process money
            total = payment()

            # if enough money was paid, deduct ingredients, give change, give drink
            if total >= MENU[beverage]["cost"]:
                process_order(beverage, total)
            # not enough money paid
            else:
                print("psh! that's not enough money!")



