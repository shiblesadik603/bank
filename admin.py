from user import User

class Admin:
    def __init__(self):
        self.users = []
        self.admin_email='admin@gmail.com'
        self.admin_password='admin'
        self.loan_enabled = True

    def create_user_account(self, email, password):
        new_user = User(email, password)
        self.users.append(new_user)
        print("User account created successfully.")

    def check_total_available_balance(self):
        # total_balance = sum(user.balance for user in self.users)
        total_balance=0
        for user in self.users:
            total_balance+=user.balance
        return total_balance

    def check_total_loan_amount(self):
        total_loan = sum(user.balance for user in self.users if user.balance < 0)
        return total_loan

    def toggle_loan_feature(self):
        self.loan_enabled = False if self.loan_enabled else True

    def get_all_users(self):
        return self.users