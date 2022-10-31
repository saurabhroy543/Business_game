class Bank:
    initial_balance = 5000
    current_bal = 0

    def bank_bal(self):
        self.current_bal = self.initial_balance

    def deposit(self, fine):
        self.current_bal += fine

    def withdraw(self, lottery):
        self.current_bal -= lottery

    def get_current_bal(self):
        return self.current_bal
