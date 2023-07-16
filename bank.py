class Bank:
    def __init__(self):
        self.customers = []
    def logged_in(self,user):
        self.customers.append(user)
    
    def check_if_user_logged_in(self,email,password):
        for user in self.customers:
            if user.email == email and user.password == password:
                return user
        return None

from user import User
from admin import Admin
  
if __name__ == "__main__":
    admin = Admin()
    bank_system = Bank()
    while True:
        print("Enter 1 to Create Bank Account")
        print("Enter 2 to Login in Bank System")
        p=int(input(''))

        if p==1:
            user_email=input('Enter your email: ')
            user_password=input('Enter your password: ')
            admin.create_user_account(user_email,user_password)

        else:
            email = input(f"Enter email for account: ")
            password = input(f"Enter password for account: ")

            if email == 'admin@gmail.com' and password == 'admin':
                while True:
                    print('Please select your desire option.')
                    print('1.check_total_available_balance')
                    print('2.check_total_loan_amount')
                    print('3. Toggle Loan Feature')
                    print('4.Stop')
                    option=int(input(''))

                    if option == 1:
                        print(f'available balance: {admin.check_total_available_balance()}')
                    elif option == 2:
                        print(f'available loan balance: {admin.check_total_loan_amount()}')
                    elif option == 3:
                        admin.toggle_loan_feature()
                    else:
                        break
            else:
                current_user = bank_system.check_if_user_logged_in(email,password)
                if current_user == None:
                    all_users = admin.get_all_users()
                    for user in all_users:
                        if email == user.email and password == user.password:
                            current_user=User(user.email,user.password)
                            bank_system.logged_in(current_user)
                    
                    if current_user == None:
                        print("Invalid Credentials")
                    else:    
                        print(f"Welcome, {email}!")
                        while True:
                            print('Please select your desire option.')
                            print('1.Deposit')
                            print('2.Withdraw')
                            print('3.Transfer_Money')
                            print('4.Available_Balance')
                            print('5.Transactions')
                            print('6.Loan')
                            print('7.Stop')
                            option=int(input(''))

                            # Perform banking services using the active_user
                            if option == 1:
                                amount=int(input('Enter amount: '))
                                current_user.deposit(amount)
                            elif option == 2:
                                amount=int(input('Enter amount: '))
                                current_user.withdraw(amount)
                            elif option == 3:
                                amount=int(input('Enter amount: '))
                                recipient=input('Enter email: ')
                                current_user.transfer(recipient,amount)
                                for user in all_users:
                                    if recipient==user.email:
                                        current_user.transaction_history.append(f"Transferred: {amount} to {user.email}")
                                        user.balance += amount
                                        break
                            elif option == 4:
                                print(f"Your Account Balance: {current_user.check_balance()}")
                            elif option == 5:
                                print(f"Your Transaction History: {current_user.check_transaction_history()}")
                            elif option == 6:
                                if admin.loan_enabled:
                                    current_user.take_loan()
                                else:
                                    print("The loan feature is currently disabled.")
                            else:
                                print('Thanks for using Bank services... ')
                                break


                        
