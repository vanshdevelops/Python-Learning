#Write a Program to find out whether a student has passed or faied if it requires a 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))

#Checking for total percentage
total_Percentage = (100 * (marks1 + marks2 + marks3)) / 300
if(total_Percentage>=40):
     print("You are Passed")

else:
    print("You are Failed, Try again next year")     