f = open("file.txt")
print(f.read())
f.close()

# the same thing can be written using the "WITH" statement without the Close function :

with open("file.txt") as f:
    print(f.read())


