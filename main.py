from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_obj = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

machine_on = True

while machine_on:
    choice = input(f"What would you like? ({menu_obj.get_items()}): ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffee.report()
        money.report()
    else:
        drink = menu_obj.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)