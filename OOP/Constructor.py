class Employee:
    language = "Python" #This is class attribute
    salary = 2000000


    def __init__(self, name, salary, language):   # dunder method which is automatically called 
        self.name = name
        self.salary = salary
        self.language = language
        print("I'm Creating an object")




    def getinfo(self):
        print(f"Language is {self.language} and salary is {self.salary}")

    @staticmethod
    def greet():
        print("Hello, Good Morning")   



Vansh = Employee("Vansh", 2000000, "C++") 
# Vansh.language = "C++" # This is object of class Employee or Instance Attribute
print(Vansh.name, Vansh.salary, Vansh.language)