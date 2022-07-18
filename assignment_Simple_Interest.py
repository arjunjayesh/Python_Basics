def interest(p,t,r):
    i=(p*t*r)/100
    return i

x=float(input("Enter the Principal Amount: ₹"))
y=float(input("Enter the Term in Years: "))
z=float(input("Enter the Annual Rate of Interest: "))

print("Simple Interest for ₹",x, "taken for a span of", y, "Years at", z, "% per annum is ₹", interest(x,y,z))