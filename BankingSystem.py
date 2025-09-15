import re
import random
#helps verify text and message
account_id = 0
bank = 0
pockets = 0

class Bank:
    class BankInfo:
        def __init__(self, first_name, last_name, account_id, pin, balance=0, pockets=0):
            self.first_name = first_name
            self.last_name = last_name
            self.account_id = account_id
            self.pin = pin
            self.balance = balance
            self.pockets = pockets

        def deposit(self, amount):
            self.balance  += amount
            print(f"${amount} deposited successfully.")
            return self.balance

        def withdraw(self, amount):
            if amount > self.balance:
                print("Insufficient bank balance.")
                return self.balance
            self.balance -= amount
            print(f"${amount} withdrawn from bank balance.")
            return self.balance

        def display_balance(self):
            print('Bank Balance for account ID ' + str(self.account_id) + ' is $' + str(self.balance) + '; Cash in pockets: $' + str(self.pockets))

    @staticmethod
    def valid_name(name):
        # makes it so its only letters and dashes (-),
        return bool(re.fullmatch(r"[A-Za-z\-]+", name))

    @staticmethod
    def valid_account_id(aid):
        # checks if its only 8 digits 
        return bool(re.fullmatch(r"\d{8}", aid))

    @staticmethod
    def valid_pin(pin):
        # only 6 digits basically the same as 8 thingy
        return bool(re.fullmatch(r"\d{6}", pin))

accounts = {}

def get_account(account_id):
    return accounts.get(account_id)

def generate_random_account_id():
    # gENERates an 8 digit account id number 
    while True:
        new_id = "{:08d}".format(random.randint(0, 99999999))
        if new_id not in accounts:
            return new_id

def create_account():
    while True:
        FN = input("Enter your first name: ")
        if Bank.valid_name(FN):
            break
        else:
            print("Invalid name. Use letters and hyphens only.")
    while True:
        LN = input("Enter your last name: ")
        if Bank.valid_name(LN):
            break
        else:
            print("Invalid name. Use letters and hyphens only.")
    while True:
        new_account_id = generate_random_account_id()
        print(f"Here is your new account ID: {new_account_id}. Remember this you will need it later.")
        break
        if new_account_id in accounts:
            print("Account ID already exists.")
            try_new = input("Do you want to try a different ID? (y/n): ").lower()
            if try_new == 'y':
                continue
            else:
                return None
        else:
            break
    while True:
        pin = input("Please enter 6-digit pin: ")
        if Bank.valid_pin(pin):
            break
        else:
            print("Invalid pin. Must be 6 digits.")
    new_acc = Bank.BankInfo(FN, LN, new_account_id, pin)
    accounts[new_account_id] = new_acc
    print(f"Account created for {FN} {LN}.")
    return new_acc

def main():
    while True:
        acc_id = input("Enter your 8-digit account ID to login or press Enter to create new account: ")
        if acc_id == "":
            account = create_account()
            if account is not None:
                break
            else:
                continue
        elif Bank.valid_account_id(acc_id):
            account = get_account(acc_id)
            if account:
                print(f"Account found for {account.first_name} {account.last_name} (ID: {account.account_id})")
                pin_attempts = 3
                while pin_attempts > 0:
                    pin = input("Enter your 6-digit pin: ")
                    if pin == account.pin:
                        print("Pin correct! Access granted.")
                        break
                    else:
                        pin_attempts -= 1
                        print("Pin wrong.")
                        if pin_attempts == 0:
                            print("Pin attempts exceeded.")
                            create_new = input("Do you want to create an account with a different account number? (y/n): ").lower()
                            if create_new == 'y':
                                account = create_account()
                                if account is not None:
                                    break
                                else:
                                    pin_attempts = 3
                            else:
                                pin_attempts = 3 # User gets 3 attempts beofre  reset 
                if pin_attempts > 0:
                    break
            else:
                print("Account ID not found.")
                create_new = input("Would you like to create a new account? (y/n): ").lower()
                if create_new == 'y':
                    account = create_account()
                    if account is not None:
                        break
                else:
                    print("Goodbye! Hope to see you again soon.")
                    exit()
        else:
            print("Invalid account ID. Must be 8 digits.")
    print("What would you like to do select from the following")
    print("1) Deposit")
    print("2) Withdraw")
    print("3) Transfer from pockets to bank")
    print("4) Display_balance")
    print("5) Exit")
    choice = input("Choice (1-5): ")
    if choice == "1":
        amt = float(input("Amount to deposit: "))
        account.deposit(amt)
    elif choice == "2":
        amt = float(input("Amount to withdraw from bank: "))
        account.withdraw(amt)
    elif choice == "3":
        amt = float(input("Amount to transfer from pockets to bank: "))
        if amt > account.pockets:
            print("Insufficient cash in pockets to transfer.")
        else:
            account.pockets -= amt
            account.balance += amt
            print(f"${amt} transferred from pockets to bank.")
    elif choice == "4":
        account.display_balance()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
