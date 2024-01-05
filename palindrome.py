def palin(n):
       st=str(n)
       rev=st[::-1]   
       if  rev==st:
            return True
       else:
            return False
n=input("enter the number:")
result=palin(n)
if  result==True:
     print("it is palindrome")
else:
     print("not a palindrome")

  
