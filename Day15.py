MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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
    "money":0
}
COINS={"quarters":0.25,
       "dimes":0.10,
       "nickles":0.05,
       "pennies":0.01
}
def make_payement():
    print("Please insert coins.")
    quarters = int(input(f"How many quarters ? :"))
    dimes = int(input(f"How many dimes ? :"))
    nickles = int(input(f"How many nickles ? :"))
    pennies = int(input(f"How many pennies ? :"))

    return quarters,dimes,nickles,pennies


def transaction_calculator(quarters,dimes,nickles,pennies,order):
    order = MENU[order]["cost"]
    quarters=COINS["quarters"]*quarters
    dimes=COINS["dimes"]*dimes
    nickles=COINS["nickles"]*nickles
    pennies=COINS["pennies"]*pennies
    total=quarters+dimes+nickles+pennies

    if order<(total):
        resources["money"]=resources["money"]+order
        return round(total-order,2)
    else :
        return round(total-order,2)

def resource_manager(order):
    order = MENU[order]["ingredients"]
    resources["water"] = resources["water"] - order["water"]
    resources["milk"] = resources["milk"] - order["milk"]
    resources["coffee"] = resources["coffee"] - order["coffee"]
def avail_resources(order):
    order=MENU[order]["ingredients"]
    if resources["water"]-order["water"]<=0 or resources["milk"]-order["milk"]<=0 or resources["coffee"]-order["coffee"]<=0:

        return False
    else:
        return True

def main():
    while True:
        order=input('What would you like? (espresso/latte/cappuccino):').lower()
        if order=="espresso":
            if avail_resources(order):
                pay=make_payement()
                change=transaction_calculator(pay[0],pay[1],pay[2],pay[3],order)
                if change>0:
                    resource_manager(order)
                    print(f"Here is ${change} in change .")
                    print(f"Here is your {order} ☕ Enjoy!")
                elif change<0:
                    print("Sorry that's not enough money.Money refunded.")

        elif order=="latte":
            if avail_resources(order):
                pay = make_payement()
                change = transaction_calculator(pay[0], pay[1], pay[2], pay[3],order)
                if change > 0:
                    resource_manager(order)
                    print(f"Here is ${change} in change .")
                    print(f"Here is your {order} ☕ Enjoy!")
                elif change < 0:
                    print("Sorry that's not enough money.Money refunded.")

        elif order=="cappuccino":
            if avail_resources(order):
                pay=make_payement()
                change=transaction_calculator(pay[0],pay[1],pay[2],pay[3],order)
                if change>0:
                    resource_manager(order)
                    print(f"Here is ${change} in change .")
                    print(f"Here is your {order} ☕ Enjoy!")
                elif change<0:
                    print("Sorry that's not enough money.Money refunded.")
        elif order=="report":
            for _ in resources:
                print(f"{_}: {resources[_]}")

        elif order=="off":
            print("Turning off")
            break



if __name__=="__main__":
    main()
