from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    choice = input(f"What would you like? {menu.get_items()}? ").lower()
    if choice == 'off':
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        find_drink = menu.find_drink(choice)
        resource_sufficient = coffee_maker.is_resource_sufficient(find_drink)

        if resource_sufficient and money_machine.make_payment(find_drink.cost):
                coffee_maker.make_coffee(find_drink)
