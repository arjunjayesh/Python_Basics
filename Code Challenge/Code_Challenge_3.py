def BMCalc(a,b):
    BMI=a/(b**2)
    return BMI
x=float(input("Enter the Height: "))
y=float(input("Enter the Weight: "))
print("BMI is : ", BMCalc(x,y))