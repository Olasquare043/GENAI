# importing bank class for operation/functions
import BankClass as Bank
print("")
print("==============================================================")
print("============== Welcome to Olasquare Bank =====================")
print("==============================================================")
print()
print("Let first create account for you.....")
# creatin account
name=input("Enter account fullname: ")
account_type=input("Which Account type you want to open (Savings/Current)?: ")
initial_deposit=input("Enter initial deposit: ")
try:
    initial_deposit=float(initial_deposit)    
except ValueError:
    print("Invalid intial deposit.. Setting to 0")
    initial_deposit=0.0

# Creating account
msg,Account1= Bank.BankAccount.create_account(name,account_type,initial_deposit)
print("")
print(msg)

# Loop for repeating operations
while True:
    print("")
    print("==============================================================")
    print("Select operation to Perform")
    # print("1. Create Account")
    print("1. Deposit ")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")
    print("--------------------------------------")
    print("")
    choice= input("Enter your choice of operation: ")
    # checking the selected choice
    if choice=='1':
        amount=input("Enter amount to deposit: ")
        try:
            amount= float(amount)
        except ValueError:
            print("invalid input")
            continue
        print(Account1.deposit(amount))
    elif choice=='2':
        amount=input("Enter amount to withdraw: ")
        try:
            amount= float(amount)
        except ValueError:
            print("invalid input")
            continue
        print(Account1.withdraw(amount))
    elif choice=='3':
        print(Account1.check_balance())
    elif choice=='4':
        break
    else:
        print("Invalid choice selected")
print("")
print("==============================================================")
print("============= Thanks for using Olasquare program =============")
print("==============================================================")
print()


