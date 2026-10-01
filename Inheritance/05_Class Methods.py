# class Employee:
#     a = 5
#     def show(self):
#         print(f"The class value of a is {self.a}")


# e = Employee()
# e.a = 50 # 
# e.show() # It will print the value of a as 50 because we have changed the value of a in the object e. 



class Employee:
    a = 5
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")



    @property # It is a method decorator which is used to define a property method. It takes the instance as the first argument.
    def name(self):
        return f"{self.fname} {self.flname}" # It will return the name and surname of the employee. We are using _name and _surname to make them private variables.



    @name.setter # It is a method decorator which is used to define a setter method. It takes the instance as the first argument.
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.flname = value.split(" ")[1]


e = Employee()
e.a = 50

e.name = "Vansh Prajapati"
print(e.name) # printing the name of the employee


e.show()