def add(n1,n2):
      return n1+n2
def subtract(n1,n2):
        return n1-n2
def multiply(n1,n2):
        return n1*n2
def  division(n1,n2):
         if n2==0:
              print("division is not possible:")
         else:
                 return n1/n2
def power(n1,n2):
                 return n2**n1
def calculator(n1,op,n2):
        if op=="+":
             return add(n1,n2)
        elif op=="-":
             return subtract(n1,n2)
        elif op=="*":
              return multiply(n1,n2)
        elif op=="/":
              return division(n1,n2)
        elif op=="**":
              return power(n1,n2)
        else:
              print("enter a valid operation")
print("operations are : \n+ for addition \n- for subtraction\n* for multiplication\n/ for division \n** for power")
n1=int(input("enter the first number: "))
n2=int(input("enter the second number: "))
op=str(input("enter the operation: "))
result=calculator(n1,op,n2)
print("result= ",result)
         
