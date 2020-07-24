# coffee-machine.py
#jetbrains academy project

def start():
    while True:        
        global water_avl, milk_avl, beans_avl, cups_avl, money_avl 
        take_action()
 
def inventory(water=0,milk=0,beans=0,cups=0,money=0):
    global water_avl, milk_avl, beans_avl, cups_avl, money_avl, resources

    water_avl += water
    milk_avl += milk
    beans_avl += beans
    cups_avl += cups
    money_avl += money

def Print_current_state():
    print(f"""
The coffee machine has:
{water_avl} of water
{milk_avl } of milk
{beans_avl } of coffee beans
{cups_avl } of disposable cups
${money_avl } of money """)
    


def take_action():
    action = input("\nWrite action (buy, fill, take, remaining, exit): ")
    
    if action == 'buy':
        coffee_choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
        if coffee_choice == '1':
            if water_avl>=250 and milk_avl>=0 and beans_avl>=16 and cups_avl>=1:
                print("I have enough resources, making you a coffee !")                
                inventory(water = -250, milk = 0, beans = -16, cups = -1, money = 4)
            elif water_avl<250:
                print("Sorry, not enough water!")
                inventory()
            elif milk_avl<0:
                print("Sorry, not enough milk!")
                inventory()
            elif beans_avl<16:
                print("Sorry, not enough enough!")
                inventory()
            elif cups_avl<1:
                print("sorry, not enough cups !")
                inventory()
            take_action()

        elif coffee_choice == '2':
            if water_avl>=350 and milk_avl>=75 and beans_avl>=20 and cups_avl>=1:
                print("I have enough resources, making you a coffee!")
                inventory(water = -350, milk = -75, beans = -20, cups = -1, money = 7)
            elif water_avl<350:
                print("Sorry, not enough water!")
                inventory()
            elif milk_avl<75:
                print("Sorry, not enough milk!")
                inventory()
            elif beans_avl<20:
                print("Sorry, not enough enough!")
                inventory()
            elif cups_avl<1:
                print("sorry, not enough cups!")
            take_action()
            
        elif coffee_choice == '3':
            if water_avl>=200 and milk_avl>=100 and beans_avl>=12 and cups_avl>=1:
                print("I have enough resources, making you a coffee!")
                inventory(water = -200, milk = -100, beans = -12, cups = -1, money = 6)
            elif water_avl<200:
                print("Sorry, not enough water !")
            elif milk_avl<100:
                print("Sorry, not enough milk !")
            elif beans_avl<12:
                print("Sorry, not enough enough !")
            elif cups_avl<1:
                print("sorry, not enough cups !")

            take_action()
        elif coffee_choice == 'back':
            take_action()
        
    elif action == 'fill':
        fill_machine()
        take_action()
    
    elif action == 'take':
        print("I gave you $", money_avl, sep = "")
        inventory(money = -money_avl)
        take_action()
    elif action == "remaining":
        Print_current_state()
    
    elif action == 'exit':
        exit()
    start()
    
        
def fill_machine():
    inventory(water = int(input("Write how many ml of water do you want to add:\n")))
    inventory(milk = int(input("Write how many ml of milk do you want to add:\n")))
    inventory(beans = int(input("Write how many grams of coffee beans do you want to add:\n"
)))
    inventory(cups = int(input("Write how many disposable cups of coffee do you want to add:\n")))
    start()
    
    
if __name__ == '__main__':
    water_avl, milk_avl, beans_avl, cups_avl, money_avl= 400, 540, 120, 9, 550
    start()




