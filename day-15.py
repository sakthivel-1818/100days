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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def coin():
    print("please input coin")
    total=int(input("how many quarters?:"))* 0.25
    total += int(input("how many dimes?:"))*0.1
    total += int(input("how many nickles?:"))*0.05
    total += int(input("how many pennies?:"))*0.01
    return total

def transaction(moneyreceived,drinkcost):
    if moneyreceived>=drinkcost:
        change=round(moneyreceived-drinkcost,2)
        print(f"here is {change} change:")
        global profit
        profit+=drinkcost
        return True
    else:
        print("sorry that's not enough money")
        return False

def resource(orders):
    for item in orders:
        if orders[item]>=resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True

def coffee(drinkname,ingredians):
    for item in ingredians:
        resources[item]-=ingredians[item]
    print(f"here is your {drinkname}")


is_start=True
while is_start:
    user=input("what would you like (espresso/latte/cappuccino)").lower()
    if user=="off":
        is_start=False
    elif user=="report":
        print(f"MILk:{resources["milk"]}")
        print(f"coffee:{resources["coffee"]}")
        print(f"water:{resources["water"]}")
        print(f"money:${profit}")
    else:
        drink = MENU[user]
        if resource(drink["ingredients"]):
            payment=coin()
            if transaction(payment,drink["cost"]):
                coffee(user,drink["ingredients"])