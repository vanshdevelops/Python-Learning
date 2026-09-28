a = int(input("Enter your age: "))

# if statement no. 1
if(a%2 == 0):
    print("Your age is even")

# if statement no. 2
if(a>= 18):
    print("You are eligible to Vote")
    print("You are eligible to Drive")

elif(a<0):
    print("You are not born yet")   



else: 
    print("You are not eligible to Vote")
    print("You are not eligible to Drive")    

print("Thank you for using this program") 
print () 