class Employee:
    language = "Python" #This is class attribute
    salary = 2000000


    def getinfo(self):
        return f"Language is {self.language} and salary is {self.salary}"
    



Vansh = Employee() 
Vansh.language = "C++" # This is object of class Employee or Instance Attribute
print(Vansh.getinfo())