marks = int(input("Enter the marks\n"))
if marks>90:
    grade = "excellent"
elif marks>=80:
    grade = "A"
elif marks>70:
    grade = "b"
elif marks>60:
    grade = "c"
elif marks>50:
    grade = "d"
else:
    grade= "F"
print("your grade is " +grade)
    