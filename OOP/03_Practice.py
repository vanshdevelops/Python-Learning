# Create a class with a class attribute x, create an object from it and set 'x'directly using object x = o. Does this change the class attribute?

class My:
    x = 5
o = My()
print(o.x) # it prints class attribute value 5 because instance attribute is not present
o.x = 20 
print(o.x) # it prints 20, but class attribute is still 5 and instance attritube is set 



