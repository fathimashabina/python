student={  }
n=int(input("enter the number of students"))
for i in range(0,n):
	 name=input("enter the name of the student:")
	 age=input("enter the age of the student:")
	 grade=input("enter  the grade of the student:")
	 student[name]=[age,grade]
print(student)

