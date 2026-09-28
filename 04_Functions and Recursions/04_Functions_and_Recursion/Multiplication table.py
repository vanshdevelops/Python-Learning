# Write a python function to print Multiplication table of a given number.
 

def table(n):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
n = int(input("Enter the no: "))
table(n)
    