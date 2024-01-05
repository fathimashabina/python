def sum(n):
        s=0
        for i in range (1,1+n):
              s+=i
        return( s)
n=int(input("enter the number:"))
r=sum(n)
print("sum is",r)
