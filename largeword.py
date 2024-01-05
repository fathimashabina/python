words=[]
limit=int(input("enter the limit of words"))
largest=None
length=0
for i in range(limit):
	word=input("enter the words:")
	words.append(word)
for i in words :
           if(len(i) >length):
            largest=i
            length=len(i)
print("the largest word is : ",largest," and the length is", len(largest))

