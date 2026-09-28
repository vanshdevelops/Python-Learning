# Write a python function to remove a given word from a list and strip it at the same time.

def remove(l,word):
    for i in l:
        l.remove(word)
        return l

l = ["Vansh","fruit","ball"]    
print(remove(l, "fruit"))
