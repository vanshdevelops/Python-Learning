#Write a program to print the star pattern using for loop.

n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" "*(n-1))
    print("*" * (2*i-1))
    print("\n")

