class BankAccount:
    all_accounts =[]
    # don't forget to add some default values for these parameters!
    def __init__(self, balance , interest_rate): 
        
        self.balance = balance
        self.interest_rate = interest_rate
        self.all_accounts.append(self)

    def deposit(self, amount):
            self.balance += amount
            return self
               
    def withdraw(self, amount):
            if self.balance >= amount :
                self.balance -= amount
            else :
                print("Insufficient funds : charging $5 fee")
                self.balance -= 5
            return self
        
    def display_account_info(self):
            return self.balance
    def yield_interest(self):
            if self.balance>0 :
                self.balance += self.balance * self.interest_rate
            return self
    @classmethod
    def display_all_accounts_info(cls):
          for account in cls.all_accounts:
                account.display_account_info()

#account_1 = BankAccount(1000, 0.02)
#account_2 = BankAccount(500, 0.05)

#account_1.deposit(400).deposit(200).deposit(100).withdraw(500).yield_interest().display_account_info()
#account_2.deposit(500).deposit(100).withdraw(100).withdraw(100).withdraw(150).withdraw(50).yield_interest().display_account_info()

#BankAccount.display_all_accounts_info()
            
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {
              "checking": BankAccount(1000 ,0.02),
              "savings": BankAccount(3000,0.05)
        } 
    
    # other methods
    
    def display_user_balance(self):
        print(f"user: {self.name} , Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"user: {self.name} , Savings Balance: {self.account['savings'].display_account_info()}")
        return self
    
    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

adrien = User("Adrien","adrien.gmail.com") 
adrien.account["checking"].deposit(100)
adrien.display_user_balance()     