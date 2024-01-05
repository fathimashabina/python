student=[]
n=int(input("enter the total  no.of students:"))
total=int(input("enter the total no.of classes:"))
for i in range(n):
        name=input("enter the name of the students:")
        b=int(input("enter the no.of classes present:"))
        percent=(b/total)*100
        student.append([percent,name])
student.sort()
print(student)
