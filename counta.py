def countw(word):
	c=0
	for i in word:
		if(i=='a'):
			c=c+1
	return c
word=input("enter the string:")
print(countw(word))
