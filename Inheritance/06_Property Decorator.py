class Employee:
    a = 5
    @property # It is a method decorator which is used to define a property method. It takes the instance as the first argument. 
    def show(self):
        print(f"The class value of a is {self.a}")


e = Employee()
e.a = 50 

e.name = "Vansh"
print(e.name) # printing the name of the employee
e.show()