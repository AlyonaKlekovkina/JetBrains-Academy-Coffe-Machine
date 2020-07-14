class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, disposable_cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money

    def __str__(self):
        return "The coffee machine has:\n{} of water \n{} of milk \n{} of coffee beans \n{} of disposable cups \n${} of money".format(self.water, self.milk, self.coffee_beans, self.disposable_cups, self.money)

    def ensure_resources(self, r_water, r_milk, r_coffee_beans, r_disposable_cups, r_money):
        if self.water - r_water >= 0 and self.coffee_beans - r_coffee_beans >= 0 and self.milk - r_milk >= 0 and self.disposable_cups - r_disposable_cups >= 0:
            self.water -= r_water
            self.milk -= r_milk
            self.coffee_beans -= r_coffee_beans
            self.disposable_cups -= r_disposable_cups
            self.money += r_money
            print("I have enough resources, making you a coffee!")
        elif self.water - r_water < 0:
            print("Sorry, not enough water")
        elif self.milk - r_milk < 0:
            print("Sorry, not enough milk")
        elif self.coffee_beans - r_coffee_beans < 0:
            print("Sorry, not enough coffee beans")
        elif self.disposable_cups - r_disposable_cups < 0:
            print("Sorry, not enough disposable cups")

    def espresso(self):
        self.ensure_resources(250, 0, 16, 1, 4)

    def latte(self):
        self.ensure_resources(350, 75, 20, 1, 7)

    def cappuccino(self):
        self.ensure_resources(200, 100, 12, 1, 6)

    def fill(self, fill_water, fill_milk, fill_coffee_beans, fill_disposable_cups):
        self.water += fill_water
        self.milk += fill_milk
        self.coffee_beans += fill_coffee_beans
        self.disposable_cups += fill_disposable_cups

    def take(self):
        print("I gave you ${}".format(self.money))
        self.money -= self.money


my_machine = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    option = input("Write action (buy, fill, take, remaining, exit): ")
    if option == 'buy':
        answer = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if answer == '1':
            my_machine.espresso()
        elif answer == '2':
            my_machine.latte()
        elif answer == '3':
            my_machine.cappuccino()
        elif answer == 'back':
            continue

    elif option == 'fill':
        filled_water = int(input("Write how many ml of water do you want to add: "))
        filled_milk = int(input("Write how many ml of milk do you want to add: "))
        filled_coffee_beans = int(input("Write how many grams of coffee beans do you want to add: "))
        filled_disposable_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
        my_machine.fill(filled_water, filled_milk, filled_coffee_beans, filled_disposable_cups)
        continue

    elif option == 'take':
        my_machine.take()

    elif option == 'remaining':
        print(my_machine)
        continue

    elif option == 'exit':
        break
