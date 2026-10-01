# Create a class 2D vector to use it to create nother class representing 3D vector.

class TWODVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")


class THREEDVector(TWODVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k 

    def show(self): 
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


o = TWODVector(1, 4)
o.show()
o2 = THREEDVector(2, 4, 5)  
o2.show()    

