sub1 = int(input("enter first subject"))
sub2 = int(input("enter second subject marks"))
sub3 = int(input("enter third subject marks"))
sub4 = int(input("enter four subject marks"))
sub5  = int(input("Enter the fifth subject marks"))
 
if(sub1<33 or sub2<33 or sub3<33 or sub4<33 or sub5<33):
    print("You are fail bacuase less than 33% in each subject")
elif(sub1+sub2+sub3+sub4+sub5)/3 <40:
    print("Your are fail in the exams beacuse of the number is less than the 40% of marks.")
else:
    print("You are passed in the exams congratulations")
     

 