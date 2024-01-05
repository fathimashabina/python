class Bankaccount:
	def  __init__(self):
		self.balance=0
	def deposit(self):
		amount=int(input("enter the amount to be deposited:"))
		self.balance=+amount
		print("amount deposited",amount)
	def withdrawl(self):
		amount=int(input("enter the amount to be withdrawl:"))
		if self.balance>=amount:
            		self.balance-=amount
		else:
			 print("insufficient balance")
	def display(self):
		print("balance: ",self.balance)
object= Bankaccount()
object.deposit()
object.withdrawl()
object.display()
