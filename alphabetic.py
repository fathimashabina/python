a=int(input("enter the number of list:"))
name=[]
for i in range(0,a):
   names=input("enter the name:")
   name.append(names)
print("\nElements in the list are:",name)
print("\n sorted element in the list are :")
for i in sorted(name):
   print(i)

