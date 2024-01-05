def power(b,e):
      if e==0:
          return 1
      elif e==1:
          return b
      else:
          return b*power(b,e-1)
b=int(input("enter the base of the power operation:"))
e=int(input("enter the exponent :"))
result=power(b,e)
print("the power of ",'b',"raise to",'e',"is: ",result)


    
