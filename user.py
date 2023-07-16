class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.balance = 0
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: {amount}")
            print(f"Deposit of {amount} successful. Current balance: {self.balance}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
            print(f"Withdrawal of {amount} successful. Current balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount for withdrawal.")

    def transfer(self, recipient, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Received: {amount} from {self.email}")
            print(f"Transfer of {amount} to {recipient} successful. Current balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount for transfer.")

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self):
        loan_amount = self.balance * 2
        amount=int(input('Enter amount: '))
        if amount < loan_amount:
            self.balance += amount
            self.transaction_history.append(f"Took a loan: {amount}")
            print(f"Loan of {amount} credited to your account. Current balance: {self.balance}")
        else:
            print('Bank can not provide you that amount of money')
            
