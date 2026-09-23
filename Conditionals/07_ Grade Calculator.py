# Write a Program to calculate the grade of a student from his marks from the following schemes.

marks = int(input("Enter your marks: "))
if marks<=100 and marks>=90:
    print("Your Grade is A+")
elif marks<=90 and marks>=80:    
    print("Your Grade is A")
elif marks<=80 and marks>=70:    
    print("Your Grade is B")
elif marks<=70 and marks>=60:    
    print("Your Grade is C")
elif marks<=60 and marks>=50:    
    print("Your Grade is D")
elif marks<50:
    print("Your Grade is F")
