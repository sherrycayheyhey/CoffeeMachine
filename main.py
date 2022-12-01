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


def payment():
    print("Please insert coins. ")
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input("How many nickles? "))
    pennies = float(input("How many pennies? "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


machine_on = True

while machine_on:
    beverage = input("What would you like? (espresso/latte/cappuccino): ")

    if beverage == "espresso":
        # check resources
        if resources["water"] < MENU[beverage]["ingredients"]["water"]:
            print("insufficient water")
        elif resources["coffee"] < MENU[beverage]["ingredients"]["coffee"]:
            print("insufficient coffee")
        # if enough resources, get money
        else:
            total = payment()
            # if enough money was paid, deduct ingredients, give change, give drink
            if total >= MENU[beverage]["cost"]:
                # deduct ingredients
                resources["water"] -= MENU[beverage]["ingredients"]["water"]
                resources["coffee"] -= MENU[beverage]["ingredients"]["coffee"]

                # give change
                change = total - MENU[beverage]["cost"]
                print(f"Here's {change} in change.")

                # give drink
                print(f"Here's your {beverage} ☕ Enjoy!")
            # not enough money paid
            else:
                print("psh! that's not enough money!")
    elif beverage == "latte":
        # check resources
        if resources["water"] < MENU[beverage]["ingredients"]["water"]:
            print("insufficient water")
        elif resources["milk"] < MENU[beverage]["ingredients"]["milk"]:
            print("insufficient milk")
        elif resources["coffee"] < MENU[beverage]["ingredients"]["coffee"]:
            print("insufficient coffee")
        # if enough resources, get money
        else:
            total = payment()
            # if enough money was paid, deduct ingredients, give change, give drink
            if total >= MENU[beverage]["cost"]:
                # deduct ingredients
                resources["water"] -= MENU[beverage]["ingredients"]["water"]
                resources["milk"] -= MENU[beverage]["ingredients"]["milk"]
                resources["coffee"] -= MENU[beverage]["ingredients"]["coffee"]

                # give change
                change = total - MENU[beverage]["cost"]
                print(f"Here's {change} in change.")

                # give drink
                print(f"Here's your {beverage} ☕ Enjoy!")
            # not enough money paid
            else:
                print("psh! that's not enough money!")
    elif beverage == "cappuccino":
        # check resources
        if resources["water"] < MENU[beverage]["ingredients"]["water"]:
            print("insufficient water 💧")
        elif resources["milk"] < MENU[beverage]["ingredients"]["milk"]:
            print("insufficient milk 🥛")
        elif resources["coffee"] < MENU[beverage]["ingredients"]["coffee"]:
            print("insufficient coffee")
        # if enough resources, get money
        else:
            total = payment()
            # if enough money was paid, deduct ingredients, give change, give drink
            if total >= MENU[beverage]["cost"]:
                # deduct ingredients
                resources["water"] -= MENU[beverage]["ingredients"]["water"]
                resources["milk"] -= MENU[beverage]["ingredients"]["milk"]
                resources["coffee"] -= MENU[beverage]["ingredients"]["coffee"]

                # give change
                change = total - MENU[beverage]["cost"]
                print(f"Here's {change} in change.")

                # give drink
                print(f"Here's your {beverage} ☕ Enjoy!")
            # not enough money paid
            else:
                print("psh! that's not enough money! 💵 ")
    elif beverage == "report":
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${resources["money"]}')
    elif beverage == "off":
        sys.exit("powering down...")
    else:
        print("that wasn't an option, fool! 🙄")
