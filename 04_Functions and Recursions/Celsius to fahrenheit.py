# Write a python program using function to convert Celcius into Fahrenheit 


def f_to_c(f):
    return 5*(f-32)/9   # celcius to fahrenheit conersion formula
f = int(input("Enter temperature in fahrenheit: "))
print(f_to_c(f))


