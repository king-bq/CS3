class Account:
    def __init__(self, accName, accNumber):
        self.accName = accName
        self.accNumber = accNumber
    def deposit(self, balance=float(0), amount=float(0)):
        self.amount = float(input("Enter amount to deposit: "))
        self.balance = balance + amount
        print("Deposit successful")
        print(self.balance)
    def withraw(self, balance, amount):
        if amount > balance:
            print("Insufficient funds")
        else:
            balance -= amount
        
class SavingsAccount(Account):
    def __init__(self, accName, accNumber):
        super().__init__(accName, accNumber)
    def addInterest(self, balance, interest):
        balance += interest
    
class Bank:
    def __init__(self, bankName):
        self.bankName = bankName
        print("Welcome to", bankName)

    def openAccount(self, balance=float(0)):
        self.accName = input("Account name: ")
        self.accNumber = input("Account number: ")
        self.accType = input("Account type (savings or checking): ")
        print("Account created")
        print(f"{self.accName} [{self.accNumber}] P {balance}")
        return

    #def showAccounts(self):

    #def closeAccount(self):

    def deposit(self, balance=float(0), amount=float(0)):
        self.amount = float(input("Enter amount to deposit: "))
        print("You are about to deposit an amount of P", self.amount)
        accNumber = input("Enter account number: ")
        print("Deposit sucessful")
        return

    #def addInterest(self):

    #def __del__(self):

mbtc = Bank("Metrobank")
mbtc.openAccount()
mbtc.deposit()

