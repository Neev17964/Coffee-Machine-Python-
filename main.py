from data import MENU
from data import resources
import time

while True:
    User_Prompt = input("What would you like? (espresso/latte/cappuccino): ")
    if(User_Prompt == 'espresso'):
        water_required = MENU["espresso"]["ingredients"]["water"]
        milk_required = MENU["espresso"]["ingredients"]["milk"]
        coffee_required = MENU["espresso"]["ingredients"]["coffee"]

        if(water_required > resources["water"]):
            print("Sorry there is not enough water")
        elif(milk_required > resources["milk"]):
            print("Sorry there is not enough milk")
        elif(coffee_required > resources["coffee"]):
            print("Sorry there is not enough coffee")
        else:
            print("Sure it is available please pay Rs 750:")
            Rs500 = int(input("Rs500: "))
            Rs200 = int(input("Rs200: "))
            Rs100 = int(input("Rs100: "))
            Rs50 = int(input("Rs50: "))
            total = Rs500*500 + Rs200*200 + Rs100*100 + Rs50*50
            change = total - 750
            if(total < 750):
                print("Sorry not enough moeny\nMoney Refunded")
            elif(total > 750):
                print(f"Here is your change {change}")
                print("Here is your ☕. ENJOY!!")
                resources["water"] -= water_required
                resources["milk"] -= milk_required
                resources["coffee"] -= coffee_required
                resources["Money"] += 750
            elif(total == 750):
                print("Here is your ☕. ENJOY!!")
                resources["water"] -= water_required
                resources["milk"] -= milk_required
                resources["coffee"] -= coffee_required
                resources["Money"] += 750

    elif(User_Prompt == "latte"):
        water_required = MENU["latte"]["ingredients"]["water"]
        milk_required = MENU["latte"]["ingredients"]["milk"]
        coffee_required = MENU["latte"]["ingredients"]["coffee"]

        if(water_required > resources["water"]):
            print("Sorry there is not enough water")
        elif(milk_required > resources["milk"]):
            print("Sorry there is not enough milk")
        elif(coffee_required > resources["coffee"]):
            print("Sorry there is not enough coffee")
        else:
            print("Sure it is available please pay Rs 900:")
            Rs500 = int(input("Rs500: "))
            Rs200 = int(input("Rs200: "))
            Rs100 = int(input("Rs100: "))
            Rs50 = int(input("Rs50: "))
            total = Rs500*500 + Rs200*200 + Rs100*100 + Rs50*50
            change = total - 900
            if(total < 900):
                print("Sorry not enough moeny\nMoney Refunded")
            elif(total > 900):
                print(f"Here is your change {change}")
                print("Here is your ☕. ENJOY!!")
                resources["water"] -= water_required
                resources["milk"] -= milk_required
                resources["coffee"] -= coffee_required
                resources["Money"] += 900
            elif(total == 900):
                print("Here is your ☕. ENJOY!!")
                resources["water"] -= water_required
                resources["milk"] -= milk_required
                resources["coffee"] -= coffee_required
                resources["Money"] += 900

    elif(User_Prompt == "cappuccino"):
        water_required = MENU["cappuccino"]["ingredients"]["water"]
        milk_required = MENU["cappuccino"]["ingredients"]["milk"]
        coffee_required = MENU["cappuccino"]["ingredients"]["coffee"]

        if(water_required > resources["water"]):
            print("Sorry there is not enough water")
        elif(milk_required > resources["milk"]):
            print("Sorry there is not enough milk")
        elif(coffee_required > resources["coffee"]):
            print("Sorry there is not enough coffee")
        else:
            print("Sure it is available please pay Rs 1200:")
            Rs500 = int(input("Rs500: "))
            Rs200 = int(input("Rs200: "))
            Rs100 = int(input("Rs100: "))
            Rs50 = int(input("Rs50: "))
            total = Rs500*500 + Rs200*200 + Rs100*100 + Rs50*50
            change = total - 1200
            if(total < 1200):
                print("Sorry not enough moeny\nMoney Refunded")
            elif(total > 1200):
                print(f"Here is your change {change}")
                print("Here is your ☕. ENJOY!!")
                resources["water"] -= water_required
                resources["milk"] -= milk_required
                resources["coffee"] -= coffee_required
                resources["Money"] += 1200
            elif(total == 1200):
                print("Here is your ☕. ENJOY!!")
                resources["water"] -= water_required
                resources["milk"] -= milk_required
                resources["coffee"] -= coffee_required
                resources["Money"] += 1200

    elif(User_Prompt == "report"):
        for i, j in resources.items():
            print(f"{i}: {j}")
    
    elif(User_Prompt == "close"):
        print("Closing Coffee Machine")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        break