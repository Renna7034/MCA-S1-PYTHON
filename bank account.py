class bank_account:
    def _init_(self,name,account_number,account_type,balance):
       self.name=name
       self.account_number=account_number
    
       self.account_type=account_type
       self.balance=balance
    def display(self): 
        print("name:",self.name)
        print("account number:",self.account_number)
        print("account type:",self.account_type)
        print("balance amount:",self.balance)
    def deposit(self,amount):
       self.balance+=amount
       if amount>0:
           print("the deposited amount is:",amount)
       else:
           print("invalid deposit amount")
    def withdrawal(self,amount): 
      if(self.balance-amount<0):
          print("insufficient amount")
      else:
          self.balance=self.balance-amount
          print("the balance is:",self.balance)

choice=0
while choice!=5:
    print("1.new customer")
    print("2.deposit")
    print("3.withdrawal")
    print("4.display")
    print("5.exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        n=input("enter name:")
        a=int(input("enter account number:"))
        t=input("enter account type(SB/C):")
        b=int(input("enter  the amount:"))
        obj_account=bank_account(n,a,t,b)
    if choice==2:
        b=int(input("enter the amount to be deposited:"))
        obj_account.deposit(b)
    if choice==3:
        b=int(input("enter the amount to be withdrawn:"))
        obj_account.withdrawal(b)
    if choice==4:
        obj_account.display()
else:
     print("program terminated")