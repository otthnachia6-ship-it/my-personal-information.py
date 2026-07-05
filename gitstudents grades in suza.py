#STUDENT GRADES IN SUZA

student_name=str(input("enter your name :"))
marks=int(input("enter your marks :") )
if marks >= 80:
    print("GRADE A")
    print("congratulations",  student_name,"you done betters")

elif marks >= 60:
     print("GRADE B")
     print("welldone",  student_name, "increse efforts")
elif marks >= 40:
     print("GRADE C")
     print("good",         student_name, "you did well")
else:
     print("FAIL")
     print("you are not serous", student_name, "please stay home with parents")
     