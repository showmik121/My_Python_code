class Atm:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        self.menu()
        
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, new_balance):
        if isinstance(new_balance, int) and new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Invalid balance! Balance must be a non-negative integer.")
            
    def get_pin(self):
        return self.__pin
    
    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN successfully set!")
        else:
            print("Invalid PIN! It must be a 4-digit number.")
    
    def menu(self):
        while True:
            print("\nWelcome to the ATM")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Set PIN")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            if choice == "1":
                print(f"Your balance is: {self.get_balance()}")
            elif choice == "2":
                amount = int(input("Enter the amount to deposit: "))
                self.set_balance(self.get_balance() + amount)
                print(f"Deposited {amount}. New balance is: {self.get_balance()}")
            elif choice == "3":
                amount = int(input("Enter the amount to withdraw: "))
                if amount <= self.get_balance():
                    self.set_balance(self.get_balance() - amount)
                    print(f"Withdrawn {amount}. New balance is: {self.get_balance()}")
                else:
                    print("Insufficient balance!")
            elif choice == "4":
                new_pin = input("Enter a new 4-digit PIN: ")
                self.set_pin(new_pin)
            elif choice == "5":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")
obj=Atm()