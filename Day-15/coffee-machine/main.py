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

QUARTERS, DIMES, NICKLES, PENNIES = 0.25, 0.10, 0.05, 0.01

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resource_enough(coffee, resource):
    out_of_resource = []
    menu = MENU[coffee]
#    if (resource['water'] < menu['ingredients']['water']) or (resource['milk'] < menu['ingredients']['milk']) or (resource['coffee'] < menu['ingredients']['coffee']):
    if (resource['water'] < menu['ingredients']['water']):
        for i in resource:
            if i in menu['ingredients'] and resource[i] < menu['ingredients'][i]:
                out_of_resource.append(i)
        return (f"Sorry there is not enough {', '.join(out_of_resource)}")    
    else: return 0

def calculate_coin(quarters, dimes, nickles, pennies, coffee):
    sum = round((QUARTERS*quarters) + (DIMES*dimes) + (NICKLES*nickles) + (PENNIES*pennies), 2)
    if sum < MENU[coffee]['cost']:
        return 0
    else: return sum

def make_coffee(coffee, coin, resource):
    menu = MENU[coffee]
    water_remain = resource['water'] - menu['ingredients']['water']
    if 'milk' in menu['ingredients']:
        milk_remain = resource['milk'] - menu['ingredients']['milk']
    else: milk_remain = resource['milk']
    coffee_remain = resource['coffee'] - menu['ingredients']['coffee']
    result = {
        "water": water_remain,
        "milk": milk_remain,
        "coffee": coffee_remain
    }
    return result

def fund(coffee, sum):
    cost = MENU[coffee]['cost']
    sum = sum - cost
    return sum

def resource_result(resource, money):
    return (f"Water: {resource['water']} ml\nMilk: {resource['milk']} ml\nCoffee: {resource['coffee']} g\nMoney: ${money}")
    
def main():
    resource_remain = resources.copy()
    sum, off = 0, False
    while not off:
        user_choose = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choose in MENU:
            coffee = resource_enough(user_choose, resource_remain)
            if coffee ==0:
                print("Please insert coin.")
                quarters = float(input("How many quarters?: "))
                dimes = float(input("How many dimes?: "))
                nickles = float(input("How many nickles?: "))
                pennies = float(input("How many pennies?: "))
                
                total_coins = calculate_coin(quarters, dimes, nickles, pennies, user_choose)
                
                if total_coins == 0:
                    print("Sorry that's not enough money. Money refused.")
                else:
                    sum = fund(user_choose, total_coins)
                    coffee = resource_enough(user_choose, resource_remain)
                    
                    resource_remain = make_coffee(user_choose, total_coins, resource_remain)
                    print(f"resource_result(resource_remain, sum)\nHere is ${sum} dollars in change.")
            else:
                print(coffee)
        elif user_choose == "report":
            print(resource_result(resource_remain,sum))
        else:
            off = True
main()