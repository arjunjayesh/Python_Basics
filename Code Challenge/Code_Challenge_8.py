"""
Assume you want to build two functions for discounting products on a website.
Function number 1 is for student discount which discounts the current price to 10%.
Function number 2 is for an additional discount for regular buyers which discounts an additional 5% on the current student discounted price.
Depending on the situation, we want to be able to apply both the discounts on the products.
Design the above two mentioned functions and apply them both simultaneously on the price.
"""

def disc1(a):
    return a-(.10*a)

def disc2(b):
    return b-(.05*b)

x=float(input("Enter the Sale Amount: "))
disc=disc2(disc1(x))
print("Discounted Amount: ",disc)