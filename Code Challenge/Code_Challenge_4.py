# Write a function which would divide two numbers, design the function in a manner that it handles the divide by zero exception.
def divide(a,b):
    return a/b
try:
    x=int(input("Enter 1st Number: "))
    y=int(input("Enter 2nd Number: "))
    print(divide(x/y))
except:
    print("This is a Division byS Zero Error")