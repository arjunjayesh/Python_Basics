# Tuple

"""

* Tuples are immutable
* Tuples cannot be amended
* Tuple can be converted into a list and then converted back to a tuple

"""

x=(12,13,"hello","python")
print(type(x))

y=list(x) # convert tuple to list
print(y)
print(type(y))
y.insert(2,"Hello1")
print(y)
x=tuple(y) # convert list to tuple
print(x)
print(type(x))

for i in x: # Using for loop to display items in a tuple
    print(i)

y=(1,2,3,5) # print tuple x + tuple  together
print(x+y)

z=x*3
print(z)
