# 1. print report
# 2. Check resources sufficient?
# 3. Process coins
# 4. Check transaction successful?
# 5. Make coffee
# import library
from main import resources, MENU

# rs_water = resources['water']
# rs_milk = resources['milk']
# rs_coffee = resources['coffee']

# TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
def coffee_machine():
    like = input("What would you like? (espresso/latte/cappuccino):")    # Check the user's input to decide what to do next.
    action(like)
# The prompt should show every time action has completed (while loop)


def action(msg):
    # TODO: 2. Turn off coffee Machine by entering "off" to the prompt
    if msg == "off":
        return
    # TODO 3. Print report
    elif msg == "report":
        report()
        coffee_machine()
    # TODO 4. Check resources sufficient?
    elif msg == "espresso":
        for i in MENU['espresso']['ingredients']:
            if MENU['espresso']['ingredients'][i] > resources[i]:
                print(f"Sorry there is not enough {i}")
                return
            else:
                tot = insert_coins()
                cost = MENU['espresso']['cost']
                if cost <= tot:
                    print(f"Here is {tot-cost:.2f} in change.")
                    print("Here is your espresso. Enjoy!")
                    make_coffee('espresso')
                    coffee_machine()
                else:
                    print("Sorry that's not enough money. Money refunded.")
                break

    elif msg == "latte":
        for i in MENU['latte']['ingredients']:
            if MENU['latte']['ingredients'][i] > resources[i]:
                print(f"Sorry there is not enough {i}")
                return
            else:
                tot = insert_coins()
                cost = MENU['latte']['cost']
                if cost <= tot:
                    print(f"Here is {tot-cost:.2f} in change.")
                    print("Here is your latte. Enjoy!")
                    make_coffee('latte')
                    coffee_machine()
                else:
                    print("Sorry that's not enough money. Money refunded.")
                break

    elif msg == "cappuccino":
        for i in MENU['cappuccino']['ingredients']:
            if MENU['cappuccino']['ingredients'][i] > resources[i]:
                print(f"Sorry there is not enough {i}")
                return
            else:
                tot = insert_coins()
                cost = MENU['cappuccino']['cost']
                if cost <= tot:
                    print(f"Here is {tot-cost:.2f} in change.")
                    print("Here is your latte. Enjoy!")
                    make_coffee('cappuccino')
                    coffee_machine()
                else:
                    print("Sorry that's not enough money. Money refunded.")
                break

# TODO: 5. Process coins
def insert_coins():
    print("Please insert coins.")
    quart = int(input("how many quarters?: "))
    dim = int(input("how many dimes?: "))
    nick = int(input("how many nickles?: "))
    penn = int(input("how many pennies?: "))
    total_cost = 0.25*quart + 0.10*dim + 0.05*nick + 0.01*penn
    return total_cost

def make_coffee(coffee):
    for menu in MENU:
        if menu == coffee:
            for i in MENU[menu]['ingredients']:
                resources[i] -= MENU[menu]['ingredients'][i]
                if resources[i] < 0:
                    print(f"Sorry there not enough {i}")
                    coffee_machine()
            return resources

def report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")


coffee_machine()