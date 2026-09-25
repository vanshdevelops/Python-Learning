# Write a program to print multiplication table of a given number using for loop.


n = int(input("enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")



# Now use While Loop to do this !!

n = int(input("enter a number: "))
i = 1
while (i<=10):
    print(f"{n} x {i} = {n * i}")  

    i+=1