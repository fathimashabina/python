student={  }
ls={}
n=int(input("enter the number of students:"))
for i in range(0,n):
         name =input("enter the name of the students:")
         age=input("enter the age of the students:")
         mark=input("enter the mark of the students:")
         student[name]=[age,mark]
ls=list(student.items())
ls.sort()
print("sorting in ascending orger:",ls)
ls.sort(reverse= True)
print("sorting in descending order:",ls)
a=dict(ls)
print("the sorted order dictionary is:",a)
print("the sorted order dictionary is:",b)






