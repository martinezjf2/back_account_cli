# For this module, we will work with classes by creating a banking program. Your program will use the inheritance diagram from this week in order to create a parent class and two child classes. Your program will create an object of each type (CheckingAccount and SavingsAccount).
# Your program will use the following data:
# Balance: $200, $25
# Fees: $5
# Minimum Balance: $50
# Interest Rate: 2%
# You will need to run the program twice. Once with the account balance of $200 and once with the account balance of $25. Since the second run of the program will have a balance lower than the minimum balance, a message should be output letting the user know that their account is below the minimum balance. Incorporate the good coding practices you have learned up to this point in the course such as Try/Except Blocks, allow the user to continue to run the program, and to exit the program, formatting methods, etc.



from re import L


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = int(account_number)
        self.balance = float(balance)
        
    def getBalance(self):
        print(f"\nYour Available Balance: ${self.balance}\n")
        self.balance = float(self.balance)
        return self.balance
        
    def deposit(self, amount):
        if amount > 0:
            # setting the balance of the object to be the amount added to the balance already on the account
            self.balance += float(amount)
        print(f"\nWe are going to make a deposit of ${amount}\n")
        
    def withdrawal(self, amount):
        a = float(amount)
        if a < 0.0:
            # ValueErrors: https://docs.python.org/3/tutorial/errors.html
            raise ValueError("Amount can not be negative")
        if a > self.balance:
            raise ValueError("Do not have sufficient funds")
        self.balance -= a
        print(f"\nYou have successfully withdrawn ${a}")
        
        
        
        
class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, fees = 5, minimum_balance = 50):
        # it allows you to call methods of the superclass in your subclass, Resource: https://realpython.com/python-super/#super-in-single-inheritance 
        super().__init__(account_number,balance)
        self.fees = float(fees)
        self.minimum_balance = float(minimum_balance)
        if self.checkMinimumBalance():
            self.deductFees()
            
    # got this error: __str__ returned non-string (type NoneType) Resource that i want to implement: https://stackoverflow.com/questions/11871221/python-typeerror-str-returned-non-string-but-still-prints-to-output
    # def __str__(self):
    #     return super().__str__()
    
    # def __repr__(self):
    #     print(f"\nGreat News! You have successfully createed a Checking Account!\n")
    #     print(f"Here are the details!\n\nAccount Number: {self.account_number}\nBalance: ${self.balance}\n")
        
    def deductFees(self):
        print(f"\n${self.fees} deducted for insufficient funds\n")
        self.balance -= self.fees
        return self.balance
        
    def checkMinimumBalance(self):
        print(f"\nMinuimum Balance is ${self.minimum_balance}")
        return self.getBalance() < self.minimum_balance
        
        
        
        
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interestRate = .02):
        super().__init__(account_number, balance)
        self.interestRate = float(interestRate)
        
    def addInterest(self, interestRate = .02):
        self.balance += interestRate
        # limit to only 2 decimal places
        print(f"\nInterest Rate is 2%, Your balance is now: {round(self.balance, 2)}")
        
    # def __repr__(self):
    #     print(f"\nGreat News! You have successfully createed a Savings Account!\nHere are the details!\n\nAccount Number: {self.account_number}\nBalance: ${self.balance}\n")
       
   
   
        
        
def main():
    greeting()
    user_input()
   
def greeting():
    print("\nHello Welcome to the Smithsonian Bank!")
    print("\nPlease choose a new account to start\n")
    
    
def user_input():
    print("You can exit, by typing exit")
    number = input("\nPlease click 1 for Savings and 2 for Checking\n")
    if (number == 'exit' or number == 'Exit' or number == 'quit' or number == 'Quit' or number == 'q' or number == 'Q'):
        print("\nThank you for choosing the Smithsonian Bank! Hope you have a great day!\n")
    else: 
        check_number(number)   
    

def check_number(number):
    if number == '1' :
        chose_savings(number)
        return number
    elif number == '2' :
        chose_checking(number)
        return number
    else:
        print("\nWrong input, please choose one of the following options\n")
        user_input()    
        
        
    
def chose_checking(number):
    print("\nPlease add in the following information\n")
    id = int(input("Enter an account numnber: "))
    balance = float(input("Enter initial balance: "))
    try:
        checking = CheckingAccount(id, balance)      
        choose_options_for_checking(checking)
    except Exception as e:
        print(str(e))
    
    
    
def chose_savings(number):
    print("\nPlease add in the following information\n")
    id = int(input("Enter an account numnber: "))
    balance = float(input("Enter initial balance: "))
    try:
        savings = SavingsAccount(id, balance)
        choose_options_for_savings(savings)
    except Exception as e:
        print(str(e))
    
def choose_options_for_checking(account):
    print("\n1. Withdraw Money")
    print("2. Deposit Money")
    print("3. Get Balance")
    print("4. Deduct Fees")
    print("5. Check Minimum Balance")
    print("6. Exit")
    choice=int(input("\nEnter the choice: "))

   
    if(choice==1):
        withdrawal = float(input("\nHow much would you like to withdraw: "))
        account.withdrawal(withdrawal)
        choose_options_for_checking(account)
    elif(choice==2):
        deposit = float(input("\nHow much would you like to deposit: "))
        account.deposit(deposit)
        choose_options_for_checking(account)
    elif(choice==3):
        account.getBalance()
        choose_options_for_checking(account)
    elif(choice==4):
        account.deductFees()
        choose_options_for_checking(account)
    elif(choice==5):
        account.checkMinimumBalance()
        choose_options_for_checking(account)
    elif(choice==6):
        exit()
    else:
        print("\nInvalid choice\n")
        choose_options_for_checking(account)
        
        
def choose_options_for_savings(account):
    print("\n1. Withdraw Money")
    print("2. Deposit Money")
    print("3. Get Balance")
    print("4. Add Interest")
    print("5. Exit")
    choice=int(input("\nEnter the choice: "))

   
    if(choice==1):
        withdrawal = float(input("\nHow much would you like to withdraw: "))
        account.withdrawal(withdrawal)
        choose_options_for_savings(account)
    elif(choice==2):
        deposit = float(input("\nHow much would you like to deposit: "))
        account.deposit(deposit)
        choose_options_for_savings(account)
    elif(choice==3):
        account.getBalance()
        choose_options_for_savings(account)
    elif(choice==4):
        account.addInterest()
        choose_options_for_savings(account)
    elif(choice==5):
        exit()
    else:
        print("\nInvalid choice\n")
        choose_options_for_savings(account)
        
        
    
def exit():
    print("\nThank you for choosing the Smithsonian Bank! Hope you have a great day!\n")

    
main()