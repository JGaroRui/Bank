import ClassBank
ba=int(input("Tell me your bank account\n> "))
bank=ClassBank.Bank(ba)
decision=input("What you want to do, deposit or withdraw\n> ")
if decision=="deposit":
    amount=int(input("How much you want to deposit\n> "))
    bank.deposit(amount)
elif decision=="withdraw":
    amount=int(input("How much you want to withdraw\n> "))
    bank.withdraw(amount)
else:
    print("Please write a valid answer\n> ")
    exit(0)
print(f"Your balance {bank.getbalance()}")