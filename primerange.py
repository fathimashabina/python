lower=int(input("enter the lower limit:"))
upper =int(input("enter the upper limit:"))
print("prime numbers between",lower ,"and ",upper ,"are:")
for n in range (lower ,upper+1):
      if n>1:
           for i in range(2,n):
                    if(n%i==0):
                          break
           else:
               print(n)
          

           
