# Task 2 : Object Oriented Programming in Python

class Account:
    def __init__(self,a_number,a_holder,bal) -> None:
        self.account_number = a_number
        self.account_holder = a_holder
        self.balance = bal

    def deposit(self,amount)->None:
        self.balance+=amount

    def withdraw(self,amount)->None:
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("Error! Not Enough Balance")
    
    def get_balance(self)->float:
        return self.balance
    
    def __str__(self) -> str:
        print(f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: {self.balance}")
    
class Bank:
    def __init__(self) -> None:
        self.accounts = []

    def add_account(self,account)->None:
        for a in self.accounts:
            if a.account_number == account.account_number:
                print("Error! Account Already Exists")
                return      
        print("Account Created Successfully")       
        self.accounts.append(account)
    
    def find_account(self,account_number)->bool:
        for account in self.accounts:
            if account.account_number == account_number:
                print("Account Found")
                return True
        print("Account Not Found")
        return False 

    def list_account(self)->None:
        for account in self.accounts:
            print(f"Account Number: {account.account_number}\nAccount Holder: {account.account_holder}\nBalance: {account.balance}")
   

# Testing 
a1 = Account(1,"ABC",10000)
a1.__str__()
a1.deposit(500)
a1.__str__()
a1.withdraw(5000)
a1.__str__()

a2 = Account(2,"DEF",15000)
a3 = Account(3,"GHI",18000)

Bank_1 = Bank()
Bank_1.add_account(a1)
Bank_1.add_account(a2)
Bank_1.add_account(a3)
Bank_1.find_account(1)
Bank_1.find_account(2)
Bank_1.find_account(3)
Bank_1.find_account(4)
Bank_1.list_account()

