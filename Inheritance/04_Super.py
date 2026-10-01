class Employee:
    def __init__(self):
        print("constructor of Employee")

    a = 1

class Programmer(Employee):
    def __init__(self):
        super().__init__() # 
        print("constructor of Programmer")
    
    b = 2

class Freelancer(Employee):
    def __init__(self):
        super().__init__()
        print("constructor of Freelancer")
    
    c = 3

o = Employee
print(o.a) # printing the  value of a from Employee class

# o = Programmer
# print(o.a, o.b) # printing the value of a and b from Programmer class

# o = Freelancer 
# print(o.a, o.c) # printing the value of a and c from Freelancer class

