class Number:
    def __init__(self, num): 
        self.num = num

    def __add__(self, num): # it is a special method which is used to overload the + operator. It takes two arguments, the first one is the instance and the second one is the other operand.
        return self.num  + num.num # this will return the sum of the two numbers. We are using num.num because we are accessing the num attribute of the other operand which is an instance of the Number class.


n = Number(1)
m = Number(2) 
print(n+m)