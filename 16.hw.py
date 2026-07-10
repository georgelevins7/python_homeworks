class Bank:
    bank_name = "Bank of Georgia"
    total_accounts = 0

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    def __init__(self, owner, balance):
        self._owner = owner
        if Bank.validate_amount(balance):
            self.__balance = balance
        else:
            self.__balance = 0
        Bank.total_accounts += 1
        self.__account_number = f"AN{Bank.total_accounts:04d}"

    def deposit(self, amount):
        if Bank.validate_amount(amount):
            self.__balance += amount

    def withdrow(self, amount):
        if Bank.validate_amount(amount):
            self.__balance -= amount
    
    def check_balance(self):
        return self.__balance
    
    def get_account_number(self):
        return self.__account_number
    
    def change_owner(self, new_owner):
        self._owner = new_owner

    def owner_info(self):
        return f"Account:{self.__account_number} | Owner:{self._owner}"

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts
    
o1 = Bank("Nino", 1000)
o2 = Bank("Gio", -100)
o3 = Bank("Deme", 7000)
o4 = Bank("Vaso", 3000)

o1.withdrow(300)
o1.withdrow(300)
o1.withdrow(300)
o1.withdrow(300)
o1.withdrow(300)
o2.deposit(100)
o3.withdrow(1000)
o4.withdrow(200)
o1.deposit(395)

print(o1.check_balance())
print(o2.check_balance())
print(o3.check_balance())
print(o4.check_balance())
print(o4.owner_info())