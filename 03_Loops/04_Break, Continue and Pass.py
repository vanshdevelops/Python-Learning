for i in range(500):
    if i == 160:
        break # immediately terminates the loop, even if the loop could continue.
    print(i) 



for i in range(500):
    if i == 160:
        continue # skips the current iteration and continues with the next iteration of the loop.
    print(i)    


for i in range(500):
    if i == 160:
        pass # do nothing for now.   
    print(i) 





for i in range(500):
    pass # do nothing for now.


i = 0
while(i<500):   
    print(i)
    i += 1
