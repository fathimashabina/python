string=input("enter the string to be  replaced:")
print("string before replacing:",string)
z=string[0]
replaced=z+string[1:].replace(z,"$")
print("string after replacing:",replaced)
