"""
Write Python code which accepts name of a product and in turn returns their respective prices.
Make sure to use dictionaries to store products and their respective prices.
The dictionary should include at least 5 elements.

"""

dict = {} # Declaring an empty Dictionary

def add(x,y):
    dict.update({x:y})

z=int(input("Enter the Number of items to be added: "))
for i in range(z):
    a=input("Enter the Item Name: ")
    b=input("Enter the Item Price: ")
    add(a,b)

print(dict)
