#Write a proram to calculate the factorial of a given number suing FOR and While loop.

n = int(input("Enter the number: "))
factorial = 1
for i in range (1, n+1):
    factorial = factorial*i
print(factorial)   



# Using while loop
n = int(input("Enter the number: "))
factorial = 1
i = 1
while(i<=n):
    factorial = factorial*i
    i+=1
print(factorial)
 

