"""
Calculate the value of mathematical expression x*(x+5)^2 where x= 5 using lambda expression
"""

result=lambda x:x*(x+5)**2

x=int(input("Enter the Value for X: "))
print(result(x))