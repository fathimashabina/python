def fact(n):
      if n==1 or n==0:
             return 1
      else:
          return n*fact(n-1)
n=int(input("enter the number:"))
factorial=fact(n)
print("factorial of ",n,"is: ",factorial)
