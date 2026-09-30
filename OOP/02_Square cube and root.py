# Write a class for calculating the square cube and root of a number.

class Calculator:
    def __init__(self, number):
        self.number = number
    def square(self):
        self.square = self.number ** 2
    def cube(self):
        self.cube = self.number ** 3
    def squareroot(self):
        self.root = self.number ** 0.5

C = Calculator(16)

C.square()
C.cube()
C.squareroot()
print(C.square)
print(C.cube)
print(C.root)

