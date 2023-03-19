#Grade Determiner
#get marks from student as input
marks=int(input("Enter marks obtained: "))

if marks >=90:
    print("Student scored "+str(marks)+ " marks and his grade is A")
elif marks>=80:
    print("Student scored "+str(marks)+ " marks and his grade is B")
elif marks>=70:
    print("Student scored "+str(marks)+ " marks and his grade is C")
elif marks>=60:
    print("Student scored "+str(marks)+ " marks and his grade is D")
else:
    print("Student scored "+str(marks)+ " marks and his grade is F")
