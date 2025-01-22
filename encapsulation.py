class Atmmachine:
    def __init__(self):
        self.pin = ""  # Use string for consistent pin handling
        self.__balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
Hi, how can I help you?
1. Press 1 to create a pin
2. Press 2 to change the pin
3. Press 3 to check the balance
4. Press 4 to withdraw
5. Press anything else to exit
""")
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.change_pin()
        elif user_input == "3":
            self.check_balance()
        elif user_input == "4":
            self.user_withdraw()
        else:
            print("Exiting. Have a great day!")
            exit()

    def create_pin(self):
        user_pin = input("Enter your pin: ")
        self.pin = user_pin
        print("Pin created successfully!")
        user_balance = int(input("Enter initial balance: "))
        self.__balance = user_balance
        self.menu()

    def change_pin(self):
        old_pin = input("Enter your old pin: ")
        if old_pin == self.pin:
            new_pin = input("Enter new pin: ")
            self.pin = new_pin
            print("Your pin changed successfully!")
        else:
            print("Invalid pin!")
        self.menu()

    def user_withdraw(self):
        withdraw = int(input("How much do you want to withdraw: "))
        if withdraw <= self.balance:
            user_pin = input("Enter your pin: ")
            if user_pin == self.pin:
                self.__balance -= withdraw
                print(f"You successfully withdrew {withdraw} tk!")
            else:
                print("Invalid pin!")
        else:
            print("Insufficient balance!")
        self.menu()

    def check_balance(self):
        user_pin = input("Enter your pin: ")
        if user_pin == self.pin:
            print(f"Your balance is {self.__balance} tk.")
        else:
            print("Invalid pin!")
        self.menu()


# Instantiate the object
obj = Atmmachine()
obj.__balance="hello"
obj.check_balance()
obj._Atmmachine__="hello"
 