
def deposit(transactions, amount, balance):
    balance = balance + amount
    transactions.append(amount)
    return balance 

def withdraw(transactions, amount, balance):
    balance = balance - amount
    transactions.append(-amount)
    return balance

def check_balance(balance):
    print("Your balance = ", balance)
    pass

def print_transactions(transactions):
    print(transactions)
    pass


balance = 0
transactions = []

while True:
    print("\nBanking Options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. List transactions")
    print("5. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        amount = float(input("How much do you want to deposit?"))
        if amount < 0:
            print("Write a positive number")
        elif isinstance(amount, (int, float)):
            balance = deposit(transactions, amount, balance)
        
        else: print("Not a number. Please enter a number.")
        pass
    elif choice == '2':
        amount = float(input("How much do you want to withdraw?"))
        if amount > balance:
            print("You don't have money for this")
        else: balance = withdraw(transactions, amount, balance)
        pass
    elif choice == '3':
        check_balance(balance)
        pass
    elif choice == '4':
        print_transactions(transactions)
        pass
    elif choice == '5':
        print("Exiting the banking system. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
