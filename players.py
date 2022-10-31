class Player:
    initial_balance = 1000
    initial_position = 0
    current_bal = None
    total_steps = 0
    total_property = None

    def player(self):
        self.current_bal = self.initial_balance
        self.total_steps = self.initial_position
        self.total_property = 0

    def set_current_bal(self, new_bal):
        self.current_bal = new_bal

    def withdraw(self, fine):
        self.set_current_bal(self.current_bal - fine)

    def deposit(self, money):
        self.set_current_bal(self.current_bal + money)

    def has_required_balance(self, value):
        if self.current_bal >= value:
            return True
        return False

    def step(self, moves):
        self.total_steps =self.total_steps +moves
        return self.total_steps

    def get_total_step(self):
        return self.total_steps

    def add_to_asset(self, asset_value):
        self.total_property = +asset_value
        return self.total_property
